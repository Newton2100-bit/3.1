import java.util.*;
import java.nio.file.*;

public class creating_a_file{
  public static void main(String[] args){
    Path path = Paths.get("./sample.txt");
    Path file;

    try{

      file = Files.createFile(path);
      System.out.println("File cretaed successfully.");
    }

    catch(Exception err){
      System.err.println("An error occured " + err + ".");
    }

  }
}
