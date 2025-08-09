package java.collection;
import java.util.*;

public class exampl1{
  public static void main(String[] args){
    //Note that the array is an objet and it is of static lenght.Worth noting.
    int[] my_numbers;
    my_numbers = new int[100];
    Object[] obj = new Object[10];
    obj[1] = new Book();
    obj[2] = new Student();
  }
}

class Book{

}

class Student{

}
/* THE HIERACHY OF OUR COLECTOINS
 * 1. List (interface)
 *   a. arraylist
 *   b. linkedlist
 *   c. vector 
 *   d. stack extends vector
 *
 * 2. Queue (interface)
 *
 * 3. Set (interface)
 *    a. hashset
 *    b. linkedhashset
 *
 *  4. SortedSet
 *    a.treeset
 *   THE HIERACHY OF MAPS
 *    a. Hashmap
 *    b. linkedhashmap
 *    c. hashtable

 *    sorted map(interface)
 *       d. treemap

 *
 *     *    * 
 * */
