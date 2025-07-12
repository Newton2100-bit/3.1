import threading
import queue
import time
import random
from typing import Any, Callable, Optional
from dataclasses import dataclass
from enum import Enum

class TaskStatus(Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"

@dataclass
class Task:
    """Represents a task to be processed"""
    id: str
    data: Any
    task_type: str
    priority: int = 1  # Higher number = higher priority
    status: TaskStatus = TaskStatus.PENDING
    result: Any = None
    error: Optional[str] = None
    
    def __lt__(self, other):
        # For priority queue (higher priority first)
        return self.priority > other.priority

class Worker(threading.Thread):
    """Worker thread that processes tasks"""
    
    def __init__(self, worker_id: str, task_queue: queue.PriorityQueue, 
                 result_queue: queue.Queue, task_handlers: dict):
        super().__init__()
        self.worker_id = worker_id
        self.task_queue = task_queue
        self.result_queue = result_queue
        self.task_handlers = task_handlers
        self.running = True
        self.current_task = None
        
    def run(self):
        """Main worker loop"""
        print(f"Worker {self.worker_id} started")
        
        while self.running:
            try:
                # Get task from queue (blocks until available)
                task = self.task_queue.get(timeout=1)
                self.current_task = task
                
                print(f"Worker {self.worker_id} processing task {task.id}")
                task.status = TaskStatus.PROCESSING
                
                # Process the task
                self.process_task(task)
                
                # Put result back
                self.result_queue.put(task)
                self.task_queue.task_done()
                self.current_task = None
                
            except queue.Empty:
                continue
            except Exception as e:
                if self.current_task:
                    self.current_task.status = TaskStatus.FAILED
                    self.current_task.error = str(e)
                    self.result_queue.put(self.current_task)
                    self.task_queue.task_done()
                print(f"Worker {self.worker_id} error: {e}")
    
    def process_task(self, task: Task):
        """Process a single task"""
        try:
            # Get the appropriate handler
            handler = self.task_handlers.get(task.task_type)
            if not handler:
                raise ValueError(f"No handler for task type: {task.task_type}")
            
            # Execute the task
            result = handler(task.data)
            task.result = result
            task.status = TaskStatus.COMPLETED
            
        except Exception as e:
            task.status = TaskStatus.FAILED
            task.error = str(e)
            raise
    
    def stop(self):
        """Stop the worker"""
        self.running = False

class Dispatcher:
    """Manages workers and distributes tasks"""
    
    def __init__(self, num_workers: int = 3):
        self.task_queue = queue.PriorityQueue()
        self.result_queue = queue.Queue()
        self.workers = []
        self.num_workers = num_workers
        self.task_handlers = {}
        self.completed_tasks = {}
        self.running = False
        
        # Result processor thread
        self.result_processor = None
    
    def register_task_handler(self, task_type: str, handler: Callable):
        """Register a handler function for a specific task type"""
        self.task_handlers[task_type] = handler
    
    def start(self):
        """Start the dispatcher and all workers"""
        if self.running:
            return
        
        self.running = True
        
        # Start workers
        for i in range(self.num_workers):
            worker = Worker(
                worker_id=f"worker-{i+1}",
                task_queue=self.task_queue,
                result_queue=self.result_queue,
                task_handlers=self.task_handlers
            )
            worker.start()
            self.workers.append(worker)
        
        # Start result processor
        self.result_processor = threading.Thread(target=self._process_results)
        self.result_processor.start()
        
        print(f"Dispatcher started with {self.num_workers} workers")
    
    def stop(self):
        """Stop the dispatcher and all workers"""
        if not self.running:
            return
        
        self.running = False
        
        # Stop all workers
        for worker in self.workers:
            worker.stop()
        
        # Wait for workers to finish
        for worker in self.workers:
            worker.join()
        
        # Stop result processor
        if self.result_processor:
            self.result_processor.join()
        
        print("Dispatcher stopped")
    
    def submit_task(self, task: Task):
        """Submit a task for processing"""
        self.task_queue.put(task)
        print(f"Task {task.id} submitted (priority: {task.priority})")
    
    def _process_results(self):
        """Process completed tasks"""
        while self.running:
            try:
                task = self.result_queue.get(timeout=1)
                self.completed_tasks[task.id] = task
                
                if task.status == TaskStatus.COMPLETED:
                    print(f"Task {task.id} completed successfully")
                else:
                    print(f"Task {task.id} failed: {task.error}")
                    
            except queue.Empty:
                continue
    
    def get_task_status(self, task_id: str) -> Optional[Task]:
        """Get the status of a task"""
        return self.completed_tasks.get(task_id)
    
    def get_stats(self):
        """Get dispatcher statistics"""
        completed = sum(1 for t in self.completed_tasks.values() 
                       if t.status == TaskStatus.COMPLETED)
        failed = sum(1 for t in self.completed_tasks.values() 
                    if t.status == TaskStatus.FAILED)
        pending = self.task_queue.qsize()
        
        return {
            "pending": pending,
            "completed": completed,
            "failed": failed,
            "total_processed": completed + failed
        }

# Example task handlers
def cpu_intensive_task(data):
    """Simulate CPU-intensive work"""
    n = data.get("iterations", 1000000)
    result = sum(i**2 for i in range(n))
    time.sleep(0.1)  # Simulate additional work
    return {"result": result, "iterations": n}

def io_task(data):
    """Simulate I/O work"""
    duration = data.get("duration", 1)
    time.sleep(duration)
    return {"message": f"I/O operation completed in {duration}s"}

def math_task(data):
    """Perform mathematical operations"""
    operation = data.get("operation")
    a = data.get("a", 0)
    b = data.get("b", 0)
    
    if operation == "add":
        return {"result": a + b}
    elif operation == "multiply":
        return {"result": a * b}
    elif operation == "power":
        return {"result": a ** b}
    else:
        raise ValueError(f"Unknown operation: {operation}")

# Example usage and demonstration
def main():
    # Create dispatcher
    dispatcher = Dispatcher(num_workers=3)
    
    # Register task handlers
    dispatcher.register_task_handler("cpu", cpu_intensive_task)
    dispatcher.register_task_handler("io", io_task)
    dispatcher.register_task_handler("math", math_task)
    
    # Start the dispatcher
    dispatcher.start()
    
    try:
        # Submit various tasks
        tasks = [
            Task("task-1", {"iterations": 500000}, "cpu", priority=1),
            Task("task-2", {"duration": 2}, "io", priority=3),
            Task("task-3", {"operation": "add", "a": 10, "b": 20}, "math", priority=2),
            Task("task-4", {"operation": "multiply", "a": 7, "b": 8}, "math", priority=1),
            Task("task-5", {"duration": 1}, "io", priority=2),
            Task("task-6", {"iterations": 1000000}, "cpu", priority=1),
        ]
        
        # Submit all tasks
        for task in tasks:
            dispatcher.submit_task(task)
        
        # Wait for tasks to complete
        print("\nWaiting for tasks to complete...")
        time.sleep(8)
        
        # Check results
        print("\n--- Task Results ---")
        for task in tasks:
            completed_task = dispatcher.get_task_status(task.id)
            if completed_task:
                if completed_task.status == TaskStatus.COMPLETED:
                    print(f"{task.id}: SUCCESS - {completed_task.result}")
                else:
                    print(f"{task.id}: FAILED - {completed_task.error}")
            else:
                print(f"{task.id}: STILL PROCESSING")
        
        # Show statistics
        print(f"\n--- Statistics ---")
        stats = dispatcher.get_stats()
        for key, value in stats.items():
            print(f"{key}: {value}")
            
    finally:
        # Clean shutdown
        dispatcher.stop()

if __name__ == "__main__":
    main()
