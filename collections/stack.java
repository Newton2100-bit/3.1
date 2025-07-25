package java.collections.stack;

import java.util.Stack;
public class stack{
  public static void main(String[] args){
    // THE ONLY ONE WITH THE METHOD empty().
    Stack<String> stack = new Stack<String>();
    // System.out.println("Is the stack empty. " + stack.empty());
    stack.push("Newton");
    stack.push("Irungu");
    stack.push("Mwaura");

    System.out.println(stack);
    String first_name = stack.pop();
    String second_name = stack.pop();
    System.out.println("First name => " + first_name + "\n" + "Second name =>" + second_name);
    System.out.println("The stack after poping the above data.");
    System.out.println(stack);
    System.out.println("Your last name is " + stack.peek());
    System.out.println("Stack after peeking is.");
    System.out.println(stack);
    // You can also serach in a astck to find the presence of a value.
    stack.push("Newton");
    stack.push("Irungu");
    stack.push("Mwaura");
    
    System.out.println();
    System.out.println(stack);
    System.out.println(stack.search("Newton"));
    // Worth noting that the indexing of our stack starts from zero.
    


  }
}
