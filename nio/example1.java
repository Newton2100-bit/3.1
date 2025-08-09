import java.nio.file.*;
import java.io.IOException;

public class example1{
  public static void main(String[] args){
    // Path path = Paths.get("./sample.txt");


    /* The basic idea is that we have
     * Files.<some method>( Our object path)
     **/

    /* AVAILABLE METHODS
     * 1. createDirectory()
     * 2. createFile()
     * 3. delete() - for files and directories
     * 3. deleteIfExists() trying to handle excpetion shere and there.
     * 4. copy() 
     * 5. list() - returns a lazily populated stream(entries in a directory)
     * */

    /*
     * isExecutable()
     * isHidden()
     * isReadable()
     * exists()
     * notExists()
     * size() - returns bytes
     * */

    /*
     * readAllLines()
     * readAllBytes()
     * write(Path path,byte[] bytes, OenOptions ...options)
     * */

    Path current = Paths.get("./sample");
    System.out.println("We have our path object created.");


    Path path = current; 
    try{
      path = Files.createDirectory(current);
      System.out.println("We have created a directory successfully......");
    }


    catch(IOException e){
      System.err.println("\033[90m" + e + "\033[0m");
    }

    /* try{
      Files.deleteIfExists(path);
      System.out.println("Successful deletion.");
    }

    catch(Exception e){
      System.err.println("The error occured while deleting." + e);
    }*/



    Path file;
    System.out.println("Lets try to crete a nested file.");

    try{
      Path our_file = Paths.get("./sample/java_made_file.md");
      file = Files.createFile(our_file);

      System.out.println("Success...");
    }

    catch(Exception e){
      System.out.println(e);
    }

  } 
}
