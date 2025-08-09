// package proramming.java.collections;

public class Main{
  public static void main(String[] args){
    DynamicArray dynamic_array = new DynamicArray(5);

    for(int i = 0; i < 25; ++i){
      dynamic_array.add(String.valueOf(i));
      dynamic_array.add(i);
    }

    System.out.println("Our Size : " + dynamic_array.size() + " | Capacity :" + dynamic_array.capacity());
    // System.out.println(dynamic_array);


    dynamic_array.insert(7,"77");
    System.out.println("Size : " + dynamic_array.size()  + " | Capacity :" + dynamic_array.capacity() + "\n" + "The contents " + dynamic_array);


    Object temp;
    for(int i = 0; i < 7; i++){
      temp = dynamic_array.poll();
    }


    System.out.println("Our Size : " + dynamic_array.size() + " | Capacity :" + dynamic_array.capacity());
    System.out.println(dynamic_array);

    for(int j = 0; j < 3 ; j++){

      for(int i = 0; i < 9; i++){
        temp = dynamic_array.poll();
      }


      System.out.println("Our Size : " + dynamic_array.size() + " | Capacity :" + dynamic_array.capacity());
      System.out.println(dynamic_array);
    }
  }
}
