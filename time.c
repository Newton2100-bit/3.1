#include <stdio.h>
#include <time.h>
#include <sys/resource.h>
#include <unistd.h>
#include <pthread.h>
#include <math.h>

// Function to simulate some work (CPU-intensive)
void cpu_intensive_work() {
    volatile double result = 0.0;
    for (int i = 0; i < 50000000; i++) {
        result += sqrt(i) * sin(i);
    }
}

// Function to simulate some work with sleep (wall-clock time)
void mixed_work() {
    cpu_intensive_work();
    usleep(100000); // Sleep for 100ms (0.1 second)
}

// Thread function for demonstrating thread timing
void* thread_function(void* arg) {
    printf("Thread started\n");
    cpu_intensive_work();
    printf("Thread finished\n");
    return NULL;
}

int main() {
    printf("=== C Timing Functions Comparison ===\n\n");
    
    // ================================================================
    // 1. PERF_COUNTER EQUIVALENT - High-resolution wall-clock time
    // ================================================================
    printf("1. PERF_COUNTER EQUIVALENT (CLOCK_MONOTONIC)\n");
    printf("   - Measures wall-clock time (real time that passes)\n");
    printf("   - High resolution, monotonic (never goes backwards)\n");
    printf("   - Includes time spent sleeping/waiting\n");
    printf("   - Python equivalent: time.perf_counter()\n\n");
    
    struct timespec perf_start, perf_end;
    
    // Get starting time point
    clock_gettime(CLOCK_MONOTONIC, &perf_start);
    
    // Do some work that includes both CPU work and sleeping
    mixed_work();
    
    // Get ending time point
    clock_gettime(CLOCK_MONOTONIC, &perf_end);
    
    // Calculate elapsed wall-clock time
    double wall_time = (perf_end.tv_sec - perf_start.tv_sec) + 
                       (perf_end.tv_nsec - perf_start.tv_nsec) / 1e9;
    
    printf("   Wall-clock time: %.3f seconds\n", wall_time);
    printf("   (This includes CPU work + sleep time)\n\n");
    
    // ================================================================
    // 2. PROCESS_TIME EQUIVALENT - CPU time used by current process
    // ================================================================
    printf("2. PROCESS_TIME EQUIVALENT (CLOCK_PROCESS_CPUTIME_ID)\n");
    printf("   - Measures CPU time used by this process\n");
    printf("   - Does NOT include time spent sleeping/waiting\n");
    printf("   - Includes time from all threads in this process\n");
    printf("   - Python equivalent: time.process_time()\n\n");
    
    struct timespec proc_start, proc_end;
    
    // Get starting CPU time for this process
    clock_gettime(CLOCK_PROCESS_CPUTIME_ID, &proc_start);
    
    // Do the same work as before
    mixed_work();
    
    // Get ending CPU time for this process
    clock_gettime(CLOCK_PROCESS_CPUTIME_ID, &proc_end);
    
    // Calculate elapsed CPU time
    double process_time = (proc_end.tv_sec - proc_start.tv_sec) + 
                          (proc_end.tv_nsec - proc_start.tv_nsec) / 1e9;
    
    printf("   Process CPU time: %.3f seconds\n", process_time);
    printf("   (This excludes sleep time - only actual CPU work)\n\n");
    
    // ================================================================
    // 3. ALTERNATIVE: getrusage() for detailed process statistics
    // ================================================================
    printf("3. ALTERNATIVE: getrusage() for detailed process info\n");
    printf("   - Provides detailed resource usage statistics\n");
    printf("   - Separates user time vs system time\n");
    printf("   - Also provides memory usage, context switches, etc.\n\n");
    
    struct rusage usage_start, usage_end;
    
    // Get starting resource usage
    getrusage(RUSAGE_SELF, &usage_start);
    
    // Do CPU-intensive work
    cpu_intensive_work();
    
    // Get ending resource usage
    getrusage(RUSAGE_SELF, &usage_end);
    
    // Calculate user CPU time (time spent in user mode)
    double user_time = (usage_end.ru_utime.tv_sec - usage_start.ru_utime.tv_sec) +
                       (usage_end.ru_utime.tv_usec - usage_start.ru_utime.tv_usec) / 1e6;
    
    // Calculate system CPU time (time spent in kernel mode)
    double sys_time = (usage_end.ru_stime.tv_sec - usage_start.ru_stime.tv_sec) +
                      (usage_end.ru_stime.tv_usec - usage_start.ru_stime.tv_usec) / 1e6;
    
    printf("   User CPU time: %.3f seconds\n", user_time);
    printf("   System CPU time: %.3f seconds\n", sys_time);
    printf("   Total CPU time: %.3f seconds\n", user_time + sys_time);
    printf("   (Note: getrusage uses microseconds, so we divide by 1e6)\n\n");
    
    // ================================================================
    // 4. THREAD_TIME EQUIVALENT - CPU time used by current thread
    // ================================================================
    printf("4. THREAD_TIME EQUIVALENT (CLOCK_THREAD_CPUTIME_ID)\n");
    printf("   - Measures CPU time used by current thread only\n");
    printf("   - Useful in multi-threaded applications\n");
    printf("   - Python equivalent: time.thread_time()\n\n");
    
    struct timespec thread_start, thread_end;
    
    // Get starting CPU time for this thread
    clock_gettime(CLOCK_THREAD_CPUTIME_ID, &thread_start);
    
    // Do CPU work in current thread
    cpu_intensive_work();
    
    // Get ending CPU time for this thread
    clock_gettime(CLOCK_THREAD_CPUTIME_ID, &thread_end);
    
    // Calculate elapsed thread CPU time
    double thread_time = (thread_end.tv_sec - thread_start.tv_sec) + 
                         (thread_end.tv_nsec - thread_start.tv_nsec) / 1e9;
    
    printf("   Main thread CPU time: %.3f seconds\n", thread_time);
    printf("   (This measures only the current thread's CPU usage)\n\n");
    
    // ================================================================
    // 5. MULTI-THREADED EXAMPLE - Showing difference between process and thread time
    // ================================================================
    printf("5. MULTI-THREADED EXAMPLE\n");
    printf("   - Creating a separate thread to show timing differences\n");
    printf("   - Process time includes all threads\n");
    printf("   - Thread time measures only current thread\n\n");
    
    pthread_t worker_thread;
    
    // Start timing for both process and main thread
    clock_gettime(CLOCK_PROCESS_CPUTIME_ID, &proc_start);
    clock_gettime(CLOCK_THREAD_CPUTIME_ID, &thread_start);
    
    // Create a worker thread that does CPU work
    pthread_create(&worker_thread, NULL, thread_function, NULL);
    
    // Do work in main thread simultaneously
    cpu_intensive_work();
    
    // Wait for worker thread to complete
    pthread_join(worker_thread, NULL);
    
    // End timing
    clock_gettime(CLOCK_PROCESS_CPUTIME_ID, &proc_end);
    clock_gettime(CLOCK_THREAD_CPUTIME_ID, &thread_end);
    
    // Calculate times
    double multi_process_time = (proc_end.tv_sec - proc_start.tv_sec) + 
                                (proc_end.tv_nsec - proc_start.tv_nsec) / 1e9;
    
    double multi_thread_time = (thread_end.tv_sec - thread_start.tv_sec) + 
                               (thread_end.tv_nsec - thread_start.tv_nsec) / 1e9;
    
    printf("   Process CPU time (all threads): %.3f seconds\n", multi_process_time);
    printf("   Main thread CPU time only: %.3f seconds\n", multi_thread_time);
    printf("   (Process time > thread time because worker thread also used CPU)\n\n");
    
    // ================================================================
    // 6. SUMMARY OF TIME UNITS AND CONVERSIONS
    // ================================================================
    printf("6. TIME UNITS AND CONVERSIONS\n");
    printf("   - timespec struct: tv_sec (seconds) + tv_nsec (nanoseconds)\n");
    printf("   - timeval struct: tv_sec (seconds) + tv_usec (microseconds)\n");
    printf("   - 1 second = 1,000,000,000 nanoseconds (1e9)\n");
    printf("   - 1 second = 1,000,000 microseconds (1e6)\n");
    printf("   - 1 millisecond = 1,000,000 nanoseconds\n");
    printf("   - 1 microsecond = 1,000 nanoseconds\n\n");
    
    // Example of different time resolutions
    struct timespec current_time;
    clock_gettime(CLOCK_MONOTONIC, &current_time);
    
    printf("   Current time example:\n");
    printf("   - Seconds: %ld\n", current_time.tv_sec);
    printf("   - Nanoseconds: %ld\n", current_time.tv_nsec);
    printf("   - Total as double: %.9f seconds\n", 
           current_time.tv_sec + current_time.tv_nsec / 1e9);
    
    return 0;
}
