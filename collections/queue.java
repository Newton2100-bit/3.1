package java.collections;
import java.util.Queue;
import java.util.LinkedList;

public class queue{
  public static void main(String[] args){
    Queue<String> queue = new LinkedList<>();
    // System.out.println("\033[94mSuccessful queue creation.\033[0m");
    // /* AVAILABLE METHODS (no exceptions are thrown since you are polite).
    //  *  1. offer()
    //  *  2. poll()
    //  *  3. peek()
    //  *
    //  *  OLD METHODS (throws exceptions sice you are demanding).
    //  *   1. add()
    //  *   2 remove() 
    //  *   3. element()
    //  * */ 
    // if (queue.isEmpty()) {
    //   System.out.println("Queue is empty.");
    // } else {
    //   System.out.println("Queue has " + queue.size() + " elements.");
    // }
    //
    // queue.offer("Newton");
    // queue.offer("Irungu");
    // queue.offer("Mwaura");
    //
    //
    // int size = queue.size();
    // System.out.println("Queue size: " + size + ". With the following items " + "\033[096m" + queue + "\033[0m");
    //
    // System.out.println("Performing our first poll.");
    // queue.poll();
    // System.out.println(queue);
    //
    //
    // System.out.println("Performing our second poll.");
    // queue.poll();
    // System.out.println(queue);
    //
    // System.out.println("Our first peek");
    // String peek = queue.peek();
    // System.out.println("We peeked the value " + peek);
    //
    // System.out.println("We have the use of remove.");
    // String remove = queue.remove();
    // System.out.println("We removed the value " + remove);
    // System.out.println("The resultant queue is :\n");
    // System.out.println(queue);
    /* ORTHER METHODS
     *  1. size() - int
     *  2. isEmpty() - bool
     *  3. contains() - bool
     *  4. clear() - deletes the whole data structure.
     *  5. toArray() - craeets an a rray version o fyou data structure.
     * */

    // Experimenting the clear() method.
    queue.offer("ai");
    queue.offer("Machine learning");
    queue.offer("networks");
    queue.offer("Design of algorithims");

    // Test toArray()
    Object[] array = new String[100];
    array = queue.toArray();
    // System.out.println("The class of our array is : " + array.class.getSimpleName());

    int count = 1;
    System.out.println("String iteration ...");
    for(Object item : array){
      System.out.println("  " + count + ". " + item);
      count++;
    }
    
    System.out.println("The orignal values of our queue is :");
    System.out.println(queue);
    queue.clear();
    System.out.println("After clearing our queue.");
    System.out.println(queue);

    String message = "Our queue is empty we are realy sorry.";
    if (!queue.isEmpty()){
      message = "Our queue isn't empty unluckly clear() didin't work.";
    }
    System.out.println(message);


  }
}
