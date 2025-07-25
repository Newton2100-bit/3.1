package programming.java.collections;
import java.util.*;

public class priority_queue{
  public static void main(String[] args){
    // Queue<Double> queue = new PriorityQueue<>(Collections.reverseOrder());
    // queue.offer(12.0);
    // queue.offer(12.0);
    // queue.offer(27.0);
    // queue.offer(-2.1);
    // queue.offer(6.0);
    // queue.offer(20.0);
    // queue.offer(8.0);
    //
    // System.out.println("Our values in priority order are :");
    // while(!queue.isEmpty()){
    //   System.out.println("    " + queue.poll());
    Queue<String> queue = new PriorityQueue<>();
    // Can also work with Collections.reverseOrder() method.
    queue.offer("Newton");
    queue.offer("Ai");
    queue.offer("Theory of computing.");
    queue.offer("Software ngineering");
    queue.offer("irungu");
    queue.offer("Ann wanjiku");
    queue.offer("mwaura");

    while(!queue.isEmpty()){
      System.out.println(queue.poll());
    }
    

  }
}
