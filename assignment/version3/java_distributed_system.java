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
import java.io.*;
import java.net.*;
import java.util.*;
import java.util.concurrent.*;

public class LoadBalancer {
    private final int port;
    private final Map<Integer, ServerInfo> servers = new ConcurrentHashMap<>();
    private final AtomicInteger requestCounter = new AtomicInteger(0);
    private volatile boolean running = true;
    private final Timer healthCheckTimer;
    private final ExecutorService threadPool;
    
    public LoadBalancer(int port) {
        this.port = port;
        this.healthCheckTimer = new Timer(true);
        this.threadPool = Executors.newFixedThreadPool(20);
    }
    
    public void start() throws IOException {
        ServerSocket serverSocket = new ServerSocket(port);
        System.out.println("Load Balancer started on port " + port);
        
        // Start health check timer
        startHealthCheck();
        
        while (running) {
            try {
                Socket clientSocket = serverSocket.accept();
                threadPool.submit(new RequestHandler(clientSocket));
            } catch (IOException e) {
                if (running) {
                    System.err.println("Error accepting connection: " + e.getMessage());
                }
            }
        }
    }
    
    private void startHealthCheck() {
        healthCheckTimer.scheduleAtFixedRate(new TimerTask() {
            @Override
            public void run() {
                checkServerHealth();
            }
        }, 10000, 10000); // Check every 10 seconds
    }
    
    private void checkServerHealth() {
        long currentTime = System.currentTimeMillis();
        List<Integer> deadServers = new ArrayList<>();
        
        for (Map.Entry<Integer, ServerInfo> entry : servers.entrySet()) {
            ServerInfo server = entry.getValue();
            if (currentTime - server.lastHeartbeat > 15000) { // 15 seconds timeout
                deadServers.add(entry.getKey());
            }
        }
        
        for (Integer serverId : deadServers) {
            servers.remove(serverId);
            System.out.println("Removed dead server: " + serverId);
        }
    }
    
    private class RequestHandler implements Runnable {
        private final Socket clientSocket;
        
        public RequestHandler(Socket socket) {
            this.clientSocket = socket;
        }
        
        @Override
        public void run() {
            try (BufferedReader in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
                 PrintWriter out = new PrintWriter(clientSocket.getOutputStream(), true)) {
                
                String inputLine = in.readLine();
                
                if (inputLine.startsWith("HEARTBEAT:")) {
                    handleHeartbeat(inputLine);
                    out.println("ACK");
                } else {
                    // Handle client request
                    String response = forwardRequest(inputLine);
                    out.println(response);
                }
                
            } catch (IOException e) {
                System.err.println("Error handling request: " + e.getMessage());
            } finally {
                try {
                    clientSocket.close();
                } catch (IOException e) {
                    System.err.println("Error closing socket: " + e.getMessage());
                }
            }
        }
        
        private void handleHeartbeat(String heartbeatMsg) {
            // Parse: HEARTBEAT:serverId:port:currentLoad:totalRequests
            String[] parts = heartbeatMsg.split(":");
            if (parts.length == 5) {
                int serverId = Integer.parseInt(parts[1]);
                int serverPort = Integer.parseInt(parts[2]);
                int currentLoad = Integer.parseInt(parts[3]);
                long totalRequests = Long.parseLong(parts[4]);
                
                ServerInfo serverInfo = new ServerInfo();
                serverInfo.serverId = serverId;
                serverInfo.port = serverPort;
                serverInfo.currentLoad = currentLoad;
                serverInfo.totalRequests = totalRequests;
                serverInfo.lastHeartbeat = System.currentTimeMillis();
                
                servers.put(serverId, serverInfo);
                System.out.println("Heartbeat from server " + serverId + " - Load: " + currentLoad);
            }
        }
        
        private String forwardRequest(String request) {
            ServerInfo bestServer = selectBestServer();
            if (bestServer == null) {
                return "ERROR:No servers available";
            }
            
            try (Socket serverSocket = new Socket("localhost", bestServer.port);
                 PrintWriter out = new PrintWriter(serverSocket.getOutputStream(), true);
                 BufferedReader in = new BufferedReader(new InputStreamReader(serverSocket.getInputStream()))) {
                
                out.println(request);
                String response = in.readLine();
                requestCounter.incrementAndGet();
                
                System.out.println("Request " + requestCounter.get() + 
                    " forwarded to server " + bestServer.serverId);
                
                return response;
                
            } catch (IOException e) {
                return "ERROR:Failed to forward request - " + e.getMessage();
            }
        }
        
        private ServerInfo selectBestServer() {
            if (servers.isEmpty()) {
                return null;
            }
            
            // Select server with lowest current load
            return servers.values().stream()
                .min(Comparator.comparingInt(s -> s.currentLoad))
                .orElse(null);
        }
    }
    
    private static class ServerInfo {
        int serverId;
        int port;
        int currentLoad;
        long totalRequests;
        long lastHeartbeat;
    }
    
    public void stop() {
        running = false;
        healthCheckTimer.cancel();
        threadPool.shutdown();
    }
    
    public static void main(String[] args) {
        int port = args.length > 0 ? Integer.parseInt(args[0]) : 8080;
        
        LoadBalancer loadBalancer = new LoadBalancer(port);
        
        Runtime.getRuntime().addShutdownHook(new Thread(loadBalancer::stop));
        
        try {
            loadBalancer.start();
        } catch (IOException e) {
            System.err.println("Failed to start load balancer: " + e.getMessage());
        }
    }
}

// Client.java
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

// How to run the system:
// 1. Compile all files: javac *.java
// 2. Start Load Balancer: java LoadBalancer 8080
// 3. Start Servers: 
//    java Server 1 8081 localhost 8080
//    java Server 2 8082 localhost 8080
//    java Server 3 8083 localhost 8080
// 4. Run Client: java Client localhost 8080