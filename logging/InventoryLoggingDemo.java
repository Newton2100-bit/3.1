import java.util.*;
import java.util.concurrent.*;
import java.util.logging.Logger;
import java.util.logging.Level;
import java.util.logging.LogRecord;
import java.util.logging.Handler;
import java.util.logging.ConsoleHandler;
import java.util.logging.FileHandler;
import java.util.logging.Formatter;
import java.io.*;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

/**
 * Comprehensive Java Logging Example - Inventory Management System
 * Demonstrates various logging levels, handlers, formatters, and best practices
 */

// Custom Exception for Inventory Operations
class InventoryException extends Exception {
    private static final Logger logger = Logger.getLogger(InventoryException.class.getName());
    
    public InventoryException(String message) {
        super(message);
        logger.severe("InventoryException created: " + message);
    }
    
    public InventoryException(String message, Throwable cause) {
        super(message, cause);
        logger.severe("InventoryException created: " + message + ", Cause: " + cause.getMessage());
    }
}

// Product class representing inventory items
class Product {
    private static final Logger logger = Logger.getLogger(Product.class.getName());
    
    private String productId;
    private String name;
    private String category;
    private double price;
    private int quantity;
    private LocalDateTime lastUpdated;
    
    public Product(String productId, String name, String category, double price, int quantity) {
        this.productId = productId;
        this.name = name;
        this.category = category;
        this.price = price;
        this.quantity = quantity;
        this.lastUpdated = LocalDateTime.now();
        
        logger.info(String.format("New product created: [ID=%s, Name=%s, Category=%s, Price=%.2f, Quantity=%d]",
                productId, name, category, price, quantity));
    }
    
    public boolean updateQuantity(int newQuantity) {
        logger.fine("Attempting to update quantity for product " + productId + " from " + quantity + " to " + newQuantity);
        
        if (newQuantity < 0) {
            logger.warning("Attempted to set negative quantity for product " + productId + ": " + newQuantity);
            return false;
        }
        
        int oldQuantity = this.quantity;
        this.quantity = newQuantity;
        this.lastUpdated = LocalDateTime.now();
        
        logger.info(String.format("Product %s quantity updated: %d -> %d", productId, oldQuantity, newQuantity));
        
        if (newQuantity == 0) {
            logger.warning("Product " + productId + " (" + name + ") is now OUT OF STOCK!");
        } else if (newQuantity < 10) {
            logger.warning("Product " + productId + " (" + name + ") has LOW STOCK: " + newQuantity + " units remaining");
        }
        
        return true;
    }
    
    public void updatePrice(double newPrice) {
        logger.fine("Attempting to update price for product " + productId + " from " + price + " to " + newPrice);
        
        if (newPrice <= 0) {
            logger.severe("Attempted to set invalid price for product " + productId + ": " + newPrice);
            throw new IllegalArgumentException("Price must be positive");
        }
        
        double oldPrice = this.price;
        this.price = newPrice;
        this.lastUpdated = LocalDateTime.now();
        
        logger.info(String.format("Product %s price updated: %.2f -> %.2f", productId, oldPrice, newPrice));
        
        double percentChange = ((newPrice - oldPrice) / oldPrice) * 100;
        if (Math.abs(percentChange) > 20) {
            logger.warning(String.format("Significant price change for product %s: %.1f%%", productId, percentChange));
        }
    }
    
    // Getters
    public String getProductId() { return productId; }
    public String getName() { return name; }
    public String getCategory() { return category; }
    public double getPrice() { return price; }
    public int getQuantity() { return quantity; }
    public LocalDateTime getLastUpdated() { return lastUpdated; }
    
    @Override
    public String toString() {
        return String.format("Product{id='%s', name='%s', category='%s', price=%.2f, quantity=%d, lastUpdated=%s}",
                productId, name, category, price, quantity, lastUpdated.format(DateTimeFormatter.ISO_LOCAL_DATE_TIME));
    }
}

// Inventory Manager class - core business logic
class InventoryManager {
    private static final Logger logger = Logger.getLogger(InventoryManager.class.getName());
    
    private Map<String, Product> inventory;
    private Map<String, Integer> categoryStats;
    private ExecutorService executorService;
    
    public InventoryManager() {
        this.inventory = new ConcurrentHashMap<>();
        this.categoryStats = new ConcurrentHashMap<>();
        this.executorService = Executors.newFixedThreadPool(5);
        
        logger.info("InventoryManager initialized with thread pool size: 5");
        logger.config("Initial inventory capacity: " + inventory.size());
    }
    
    public void addProduct(Product product) throws InventoryException {
        logger.entering(InventoryManager.class.getName(), "addProduct", product.getProductId());
        
        if (product == null) {
            logger.severe("Attempted to add null product to inventory");
            throw new InventoryException("Cannot add null product");
        }
        
        if (inventory.containsKey(product.getProductId())) {
            logger.warning("Attempted to add duplicate product: " + product.getProductId());
            throw new InventoryException("Product with ID " + product.getProductId() + " already exists");
        }
        
        inventory.put(product.getProductId(), product);
        categoryStats.merge(product.getCategory(), 1, Integer::sum);
        
        logger.info("Product added to inventory: " + product.getProductId());
        logger.fine("Total products in inventory: " + inventory.size());
        logger.fine("Products in category '" + product.getCategory() + "': " + categoryStats.get(product.getCategory()));
        
        logger.exiting(InventoryManager.class.getName(), "addProduct");
    }
    
    public boolean removeProduct(String productId) {
        logger.entering(InventoryManager.class.getName(), "removeProduct", productId);
        
        Product removedProduct = inventory.remove(productId);
        
        if (removedProduct == null) {
            logger.warning("Attempted to remove non-existent product: " + productId);
            logger.exiting(InventoryManager.class.getName(), "removeProduct", false);
            return false;
        }
        
        // Update category stats
        String category = removedProduct.getCategory();
        categoryStats.computeIfPresent(category, (k, v) -> v > 1 ? v - 1 : null);
        
        logger.info("Product removed from inventory: " + productId);
        logger.fine("Total products in inventory: " + inventory.size());
        
        logger.exiting(InventoryManager.class.getName(), "removeProduct", true);
        return true;
    }
    
    public Product findProduct(String productId) {
        logger.fine("Searching for product: " + productId);
        
        Product product = inventory.get(productId);
        
        if (product == null) {
            logger.fine("Product not found: " + productId);
        } else {
            logger.fine("Product found: " + productId);
        }
        
        return product;
    }
    
    public List<Product> findProductsByCategory(String category) {
        logger.fine("Searching products by category: " + category);
        
        List<Product> results = inventory.values().stream()
                .filter(p -> p.getCategory().equalsIgnoreCase(category))
                .sorted(Comparator.comparing(Product::getName))
                .collect(ArrayList::new, ArrayList::add, ArrayList::addAll);
        
        logger.fine("Found " + results.size() + " products in category: " + category);
        return results;
    }
    
    public void processLowStockAlert() {
        logger.info("Processing low stock alerts...");
        
        List<Product> lowStockProducts = inventory.values().stream()
                .filter(p -> p.getQuantity() < 10)
                .sorted(Comparator.comparing(Product::getQuantity))
                .collect(ArrayList::new, ArrayList::add, ArrayList::addAll);
        
        if (lowStockProducts.isEmpty()) {
            logger.info("No low stock products found");
            return;
        }
        
        logger.warning("Found " + lowStockProducts.size() + " products with low stock:");
        
        for (Product product : lowStockProducts) {
            logger.warning(String.format("LOW STOCK ALERT: %s (%s) - Only %d units remaining",
                    product.getName(), product.getProductId(), product.getQuantity()));
        }
    }
    
    public void generateInventoryReport() {
        logger.info("Generating comprehensive inventory report...");
        
        try {
            int totalProducts = inventory.size();
            double totalValue = inventory.values().stream()
                    .mapToDouble(p -> p.getPrice() * p.getQuantity())
                    .sum();
            
            int totalItems = inventory.values().stream()
                    .mapToInt(Product::getQuantity)
                    .sum();
            
            logger.info("=== INVENTORY REPORT ===");
            logger.info("Total Products: " + totalProducts);
            logger.info("Total Items: " + totalItems);
            logger.info(String.format("Total Inventory Value: $%.2f", totalValue));
            
            logger.info("=== CATEGORY BREAKDOWN ===");
            categoryStats.entrySet().stream()
                    .sorted(Map.Entry.<String, Integer>comparingByValue().reversed())
                    .forEach(entry -> {
                        String category = entry.getKey();
                        int count = entry.getValue();
                        double categoryValue = inventory.values().stream()
                                .filter(p -> p.getCategory().equals(category))
                                .mapToDouble(p -> p.getPrice() * p.getQuantity())
                                .sum();
                        
                        logger.info(String.format("Category '%s': %d products, Value: $%.2f",
                                category, count, categoryValue));
                    });
            
            logger.info("=== TOP 5 MOST EXPENSIVE PRODUCTS ===");
            inventory.values().stream()
                    .sorted(Comparator.comparing(Product::getPrice).reversed())
                    .limit(5)
                    .forEach(p -> logger.info(String.format("%s - $%.2f", p.getName(), p.getPrice())));
            
        } catch (Exception e) {
            logger.severe("Error generating inventory report: " + e.getMessage());
            logger.log(Level.SEVERE, "Stack trace:", e);
        }
    }
    
    public CompletableFuture<Void> performBulkOperation(List<String> productIds, String operation) {
        logger.info("Starting bulk operation: " + operation + " on " + productIds.size() + " products");
        
        return CompletableFuture.runAsync(() -> {
            try {
                Thread.sleep(1000); // Simulate processing time
                
                for (String productId : productIds) {
                    Product product = findProduct(productId);
                    if (product != null) {
                        switch (operation.toLowerCase()) {
                            case "restock":
                                product.updateQuantity(product.getQuantity() + 50);
                                logger.fine("Restocked product: " + productId);
                                break;
                            case "discount":
                                product.updatePrice(product.getPrice() * 0.9);
                                logger.fine("Applied discount to product: " + productId);
                                break;
                            default:
                                logger.warning("Unknown bulk operation: " + operation);
                        }
                    } else {
                        logger.warning("Product not found during bulk operation: " + productId);
                    }
                }
                
                logger.info("Bulk operation completed: " + operation);
                
            } catch (InterruptedException e) {
                logger.severe("Bulk operation interrupted: " + e.getMessage());
                Thread.currentThread().interrupt();
            } catch (Exception e) {
                logger.severe("Error during bulk operation: " + e.getMessage());
                logger.log(Level.SEVERE, "Bulk operation exception:", e);
            }
        }, executorService);
    }
    
    public void shutdown() {
        logger.info("Shutting down InventoryManager...");
        
        executorService.shutdown();
        try {
            if (!executorService.awaitTermination(5, TimeUnit.SECONDS)) {
                logger.warning("Executor service did not terminate gracefully, forcing shutdown");
                executorService.shutdownNow();
            } else {
                logger.info("Executor service shut down successfully");
            }
        } catch (InterruptedException e) {
            logger.severe("Interrupted while waiting for executor shutdown");
            executorService.shutdownNow();
            Thread.currentThread().interrupt();
        }
        
        logger.info("InventoryManager shutdown complete");
    }
}

// Custom Formatter for structured logging
class CustomInventoryFormatter extends java.util.logging.Formatter {
    private final DateTimeFormatter timestampFormat = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss.SSS");
    
    @Override
    public String format(LogRecord record) {
        StringBuilder sb = new StringBuilder();
        
        // Timestamp
        sb.append(LocalDateTime.now().format(timestampFormat));
        sb.append(" | ");
        
        // Level
        sb.append(String.format("%-7s", record.getLevel().getName()));
        sb.append(" | ");
        
        // Thread - using getLongThreadID() instead of deprecated getThreadID()
        sb.append(String.format("Thread-%-2d", record.getLongThreadID()));
        sb.append(" | ");
        
        // Logger name (shortened)
        String loggerName = record.getLoggerName();
        if (loggerName.contains(".")) {
            loggerName = loggerName.substring(loggerName.lastIndexOf(".") + 1);
        }
        sb.append(String.format("%-15s", loggerName));
        sb.append(" | ");
        
        // Message - using getMessage() directly
        sb.append(record.getMessage());
        
        // Exception if present
        if (record.getThrown() != null) {
            sb.append("\n");
            StringWriter sw = new StringWriter();
            PrintWriter pw = new PrintWriter(sw);
            record.getThrown().printStackTrace(pw);
            sb.append(sw.toString());
        }
        
        sb.append("\n");
        return sb.toString();
    }
}

// Main application class
public class InventoryLoggingDemo {
    private static final Logger logger = Logger.getLogger(InventoryLoggingDemo.class.getName());
    
    public static void main(String[] args) {
        setupLogging();
        
        logger.info("=== INVENTORY MANAGEMENT SYSTEM STARTED ===");
        logger.config("Java version: " + System.getProperty("java.version"));
        logger.config("Operating system: " + System.getProperty("os.name"));
        
        InventoryManager inventoryManager = new InventoryManager();
        
        try {
            // Create sample products
            logger.info("Creating sample inventory...");
            
            Product laptop = new Product("LAPTOP001", "Gaming Laptop", "Electronics", 1299.99, 15);
            Product mouse = new Product("MOUSE001", "Wireless Mouse", "Electronics", 29.99, 50);
            Product keyboard = new Product("KEYB001", "Mechanical Keyboard", "Electronics", 89.99, 25);
            Product chair = new Product("CHAIR001", "Office Chair", "Furniture", 199.99, 8);
            Product desk = new Product("DESK001", "Standing Desk", "Furniture", 399.99, 5);
            Product book = new Product("BOOK001", "Java Programming Guide", "Books", 45.99, 30);
            Product pen = new Product("PEN001", "Blue Ballpoint Pen", "Office Supplies", 1.99, 100);
            
            // Add products to inventory
            inventoryManager.addProduct(laptop);
            inventoryManager.addProduct(mouse);
            inventoryManager.addProduct(keyboard);
            inventoryManager.addProduct(chair);
            inventoryManager.addProduct(desk);
            inventoryManager.addProduct(book);
            inventoryManager.addProduct(pen);
            
            // Demonstrate various operations
            logger.info("Performing inventory operations...");
            
            // Update quantities (will trigger low stock warnings)
            chair.updateQuantity(3);
            desk.updateQuantity(1);
            
            // Update prices (will trigger price change warnings)
            laptop.updatePrice(999.99); // Significant price drop
            
            // Search operations
            logger.info("Searching for electronics products...");
            List<Product> electronics = inventoryManager.findProductsByCategory("Electronics");
            logger.info("Found " + electronics.size() + " electronics products");
            
            // Process alerts
            inventoryManager.processLowStockAlert();
            
            // Generate comprehensive report
            inventoryManager.generateInventoryReport();
            
            // Demonstrate bulk operations with async processing
            logger.info("Testing bulk operations...");
            List<String> productIds = Arrays.asList("LAPTOP001", "MOUSE001", "KEYB001");
            
            CompletableFuture<Void> restockFuture = inventoryManager.performBulkOperation(productIds, "restock");
            CompletableFuture<Void> discountFuture = inventoryManager.performBulkOperation(
                Arrays.asList("CHAIR001", "DESK001"), "discount");
            
            // Wait for operations to complete
            CompletableFuture.allOf(restockFuture, discountFuture)
                .thenRun(() -> logger.info("All bulk operations completed successfully"))
                .join();
            
            // Demonstrate error handling
            logger.info("Testing error handling...");
            try {
                inventoryManager.addProduct(null); // This should throw an exception
            } catch (InventoryException e) {
                logger.warning("Caught expected exception: " + e.getMessage());
            }
            
            try {
                Product duplicateProduct = new Product("LAPTOP001", "Another Laptop", "Electronics", 1000.00, 10);
                inventoryManager.addProduct(duplicateProduct); // This should throw an exception
            } catch (InventoryException e) {
                logger.warning("Caught expected exception: " + e.getMessage());
            }
            
            // Test removal
            logger.info("Testing product removal...");
            boolean removed = inventoryManager.removeProduct("PEN001");
            logger.info("Product removal successful: " + removed);
            
            boolean removedAgain = inventoryManager.removeProduct("PEN001");
            logger.info("Second removal attempt successful: " + removedAgain);
            
            // Final report
            logger.info("Generating final inventory report...");
            inventoryManager.generateInventoryReport();
            
        } catch (Exception e) {
            logger.severe("Critical error in main application: " + e.getMessage());
            logger.log(Level.SEVERE, "Main application exception:", e);
        } finally {
            logger.info("Cleaning up resources...");
            inventoryManager.shutdown();
            logger.info("=== INVENTORY MANAGEMENT SYSTEM SHUTDOWN COMPLETE ===");
        }
    }
    
    private static void setupLogging() {
        try {
            // Remove default console handler
            Logger rootLogger = Logger.getLogger("");
            Handler[] handlers = rootLogger.getHandlers();
            for (Handler handler : handlers) {
                rootLogger.removeHandler(handler);
            }
            
            // Create console handler with custom formatter
            ConsoleHandler consoleHandler = new ConsoleHandler();
            consoleHandler.setFormatter(new CustomInventoryFormatter());
            consoleHandler.setLevel(Level.INFO);
            rootLogger.addHandler(consoleHandler);
            
            // Create file handler for all logs
            FileHandler fileHandler = new FileHandler("inventory_system.log", true);
            fileHandler.setFormatter(new CustomInventoryFormatter());
            fileHandler.setLevel(Level.ALL);
            rootLogger.addHandler(fileHandler);
            
            // Create separate file handler for errors only
            FileHandler errorHandler = new FileHandler("inventory_errors.log", true);
            errorHandler.setFormatter(new CustomInventoryFormatter());
            errorHandler.setLevel(Level.WARNING);
            rootLogger.addHandler(errorHandler);
            
            // Set root logger level
            rootLogger.setLevel(Level.ALL);
            
            // Configure specific logger levels
            Logger.getLogger(InventoryManager.class.getName()).setLevel(Level.FINE);
            Logger.getLogger(Product.class.getName()).setLevel(Level.INFO);
            
            logger.config("Logging configuration completed successfully");
            
        } catch (IOException e) {
            System.err.println("Failed to setup logging: " + e.getMessage());
            e.printStackTrace();
        }
    }
}
