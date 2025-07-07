import java.io.*;
import java.util.concurrent.atomic.AtomicInteger;
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

