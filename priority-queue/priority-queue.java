import java.util.*;
public class Main{
  public static void main(String[] args) {
    System.out.println("Hello there here is a priority queue sample");
    Queue<Double> queue = new PriorityQueue<>();
    System.out.println("Entering value sinto the queue");
    queue.offer(12.2);
    queue.offer(10.3);
    queue.offer(34.1);
    queue.offer(2.3);
    queue.offer(7.8);
    queue.offer(22.7);
    queue.offer(0.9);
    System.out.print("[");
    while(!queue.isEmpty()){
      System.out.print(queue.poll() +" ");
    }
    System.out.println("]");
  }
}
