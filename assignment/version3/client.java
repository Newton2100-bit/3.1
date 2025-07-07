import java.io.*;
import java.net.*;
import java.util.Random;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class Client {
    private final String loadBalancerAddress;
    private final int loadBalancerPort;
    private final ExecutorService threadPool;
    
    public Client(String loadBalancerAddress, int loadBalancerPort) {
        this.loadBalancerAddress = loadBalancerAddress;
        this.loadBalancerPort = loadBalancerPort;
        this.threadPool = Executors.newFixedThreadPool(10);
    }
    
    public void sendRequest(String request) {
        threadPool.submit(() -> {
            try (Socket socket = new Socket(loadBalancerAddress, loadBalancerPort);
                 PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
                 BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()))) {
                
                long startTime = System.currentTimeMillis();
                out.println(request);
                String response = in.readLine();
                long endTime = System.currentTimeMillis();
                
                System.out.println("Request: " + request);
                System.out.println("Response: " + response);
                System.out.println("Response time: " + (endTime - startTime) + "ms");
                System.out.println("---");
                
            } catch (IOException e) {
                System.err.println("Error sending request: " + e.getMessage());
            }
        });
    }
    
    public void simulateLoad(int numRequests, int intervalMs) {
        Random random = new Random();
        
        for (int i = 0; i < numRequests; i++) {
            // Generate random numbers for sum calculation
            int[] numbers = new int[5];
            StringBuilder request = new StringBuilder("SUM:");
            
            for (int j = 0; j < numbers.length; j++) {
                numbers[j] = random.nextInt(100);
                  if (j > 0) request.append(",");
                request.append(numbers[j]);
            }
            
            sendRequest(request.toString());
            
            try {
                Thread.sleep(intervalMs);
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
                break;
            }
        }
    }
    
    public void shutdown() {
        threadPool.shutdown();
    }
    
    public static void main(String[] args) {
        String loadBalancerAddress = args.length > 0 ? args[0] : "localhost";
        int loadBalancerPort = args.length > 1 ? Integer.parseInt(args[1]) : 8080;
        
        Client client = new Client(loadBalancerAddress, loadBalancerPort);
        
        // Simulate load - send 20 requests with 1 second interval
        client.simulateLoad(20, 1000);
        
        // Wait a bit then shutdown
        try {
            Thread.sleep(25000);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
        
        client.shutdown();
    }
}
