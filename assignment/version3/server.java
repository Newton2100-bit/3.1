// Server.java
import java.io.*;
import java.net.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.concurrent.atomic.AtomicLong;

public class Server {
    private final int serverId;
    private final int port;
    private final String loadBalancerAddress;
    private final int loadBalancerPort;
    private ServerSocket serverSocket;
    private volatile boolean running = true;
    private final AtomicInteger currentLoad = new AtomicInteger(0);
    private final AtomicLong totalRequests = new AtomicLong(0);
    private final ExecutorService threadPool;
    private final Timer heartbeatTimer;
    
    public Server(int serverId, int port, String loadBalancerAddress, int loadBalancerPort) {
        this.serverId = serverId;
        this.port = port;
        this.loadBalancerAddress = loadBalancerAddress;
        this.loadBalancerPort = loadBalancerPort;
        this.threadPool = Executors.newFixedThreadPool(10);
        this.heartbeatTimer = new Timer(true);
    }
    
    public void start() throws IOException {
        serverSocket = new ServerSocket(port);
        System.out.println("Server " + serverId + " started on port " + port);
        
        // Start heartbeat mechanism
        startHeartbeat();
        
        // Accept client connections
        while (running) {
            try {
                Socket clientSocket = serverSocket.accept();
                threadPool.submit(new ClientHandler(clientSocket));
            } catch (IOException e) {
                if (running) {
                    System.err.println("Error accepting client connection: " + e.getMessage());
                }
            }
        }
    }
    
    private void startHeartbeat() {
        heartbeatTimer.scheduleAtFixedRate(new TimerTask() {
            @Override
            public void run() {
                sendHeartbeat();
            }
        }, 0, 5000); // Send heartbeat every 5 seconds
    }
    
    private void sendHeartbeat() {
        try (Socket socket = new Socket(loadBalancerAddress, loadBalancerPort);
             PrintWriter out = new PrintWriter(socket.getOutputStream(), true)) {
            
            String heartbeatMsg = String.format("HEARTBEAT:%d:%d:%d:%d", 
                serverId, port, currentLoad.get(), totalRequests.get());
            out.println(heartbeatMsg);
            
        } catch (IOException e) {
            System.err.println("Failed to send heartbeat: " + e.getMessage());
        }
    }
    
    private class ClientHandler implements Runnable {
        private final Socket clientSocket;
        
        public ClientHandler(Socket socket) {
            this.clientSocket = socket;
        }
        
        @Override
        public void run() {
            currentLoad.incrementAndGet();
            totalRequests.incrementAndGet();
            
            try (BufferedReader in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
                 PrintWriter out = new PrintWriter(clientSocket.getOutputStream(), true)) {
                
                String inputLine = in.readLine();
                String response = processRequest(inputLine);
                out.println(response);
                
            } catch (IOException e) {
                System.err.println("Error handling client request: " + e.getMessage());
            } finally {
                currentLoad.decrementAndGet();
                try {
                    clientSocket.close();
                } catch (IOException e) {
                    System.err.println("Error closing client socket: " + e.getMessage());
                }
            }
        }
        
        private String processRequest(String request) {
            try {
                // Parse request - expecting "SUM:1,2,3,4,5"
                if (request.startsWith("SUM:")) {
                    String[] numbers = request.substring(4).split(",");
                    long sum = 0;
                    for (String num : numbers) {
                        sum += Long.parseLong(num.trim());
                    }
                    
                    // Simulate processing time
                    Thread.sleep(100);
                    
                    return String.format("RESULT:%d:SERVER_%d:%d", sum, serverId, System.currentTimeMillis());
                } else {
                    return "ERROR:Invalid request format";
                }
            } catch (Exception e) {
                return "ERROR:" + e.getMessage();
            }
        }
    }
    
    public void stop() {
        running = false;
        heartbeatTimer.cancel();
        threadPool.shutdown();
        try {
            if (serverSocket != null) {
                serverSocket.close();
            }
        } catch (IOException e) {
            System.err.println("Error closing server socket: " + e.getMessage());
        }
    }
    
    public static void main(String[] args) {
        if (args.length != 4) {
            System.out.println("Usage: java Server <serverId> <port> <loadBalancerAddress> <loadBalancerPort>");
            return;
        }
        
        int serverId = Integer.parseInt(args[0]);
        int port = Integer.parseInt(args[1]);
        String loadBalancerAddress = args[2];
        int loadBalancerPort = Integer.parseInt(args[3]);
        
        Server server = new Server(serverId, port, loadBalancerAddress, loadBalancerPort);
        
        // Shutdown hook for graceful shutdown
        Runtime.getRuntime().addShutdownHook(new Thread(server::stop));
        
        try {
            server.start();
        } catch (IOException e) {
            System.err.println("Failed to start server: " + e.getMessage());
        }
    }
}

// LoadBalancer.java

                
               
                
        
        
// Client.java

              

