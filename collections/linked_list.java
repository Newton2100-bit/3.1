package programming.java.collections;
import java.util.*;

public class linked_list{
  public static void main(String[] args){
    LinkedList<String> linked_list = new LinkedList<>();
    System.out.println("The given origina size is " + linked_list.size());
    // Default is a doubly linked list.
    // Maintains a head and tail varibales.
    //
    //
    /* THE SIX VERY USEFUL METHOODS IN LINKED LIETS IN JAVA.
     *
     *  NB : Canbe treated as as a stack or as a queue.
     *  1. pollFirst()
     *  2. pollLast()
     *   . poll() - returns first and deletes it.
     *
     *  3. peekFirst()
     *  4. peekLast()
     *   . peek()
     *
     *  5. offerFirst()
     *  6. offerLast()
     *   . offer() - adds at the end.
     *   COMMONLY USED IN THE CONCEPT OF LINKED LISTS.
     *  7. add(index , value)
     *  8. get(index) - returns a value by index withot removing it as we have poll do. 
     *  9. getFirst()
     *
     *
     *
     *  There exits the alternnative remove(), get() and add() methods that are exceptions prone.
     * */
    linked_list.offer("hundred");
    linked_list.offer("twenty");
    linked_list.add(1, "one");
    linked_list.add(2, "two");
    linked_list.add(3, "Three");
    linked_list.add(0, "zero");
    linked_list.add(4, "four");

    System.out.println(linked_list);
  }
}
