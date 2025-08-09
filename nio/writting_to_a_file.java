import java.nio.file.*;
import java.io.*;

public class writting_to_a_file{
  public static void main(String[] args){
    String message = "My name is newton irungu a computer science student.\n";
    Path path = Paths.get("./sample.txt");

    // try{
    //   Files.write(path, message.getBytes());
    //   System.out.println("The write was a success.");
    // }
    //
    // catch(Exception err){
    //   System.out.println("An error occured. " + err);
    // }

    try{

      for(int i = 0; i < 2 ; ++i){
        Files.write(path, message.getBytes(), StandardOpenOption.APPEND);
      }

        System.out.println("The write was a success.");
    }

    catch(Exception err){
      System.out.println("An error occured. " + err);
    }

  }
}

