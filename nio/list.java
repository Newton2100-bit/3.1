import java.nio.file.*;
import java.io.IOException;
import java.util.stream.Stream;

public class list{
    public static void main(String[] args) throws IOException {
        Path dir = Paths.get(".");

    
        try (Stream<Path> stream = Files.list(dir)) {
            stream.forEach(System.out::println);
      // System.out.println()
        }
    
  }
}
