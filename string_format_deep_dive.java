import java.util.*;
import java.time.LocalDateTime;

/**
 * Complete Guide to String.format() in Java
 * Deep dive into formatting capabilities
 */
public class StringFormatDeepDive {
    
    public static void main(String[] args) {
        System.out.println("=== STRING.FORMAT() DEEP DIVE ===\n");
        
        // Basic syntax demonstration
        demonstrateBasicSyntax();
        
        // Integer formatting
        demonstrateIntegerFormatting();
        
        // Floating point formatting
        demonstrateFloatFormatting();
        
        // String formatting
        demonstrateStringFormatting();
        
        // Date and time formatting
        demonstrateDateTimeFormatting();
        
        // Advanced formatting techniques
        demonstrateAdvancedFormatting();
        
        // Practical examples
        demonstratePracticalExamples();
    }
    
    private static void demonstrateBasicSyntax() {
        System.out.println("=== BASIC SYNTAX ===");
        
        // Basic format specifier: %[flags][width][.precision]conversion
        
        int number = 42;
        String name = "Alice";
        double price = 19.99;
        
        // Simple placeholders
        String result1 = String.format("Number: %d, Name: %s, Price: %.2f", 
                                      number, name, price);
        System.out.println(result1);
        
        // Positional arguments (1$ means first argument)
        String result2 = String.format("Name: %2$s, Number: %1$d, Price: %3$.2f", 
                                      number, name, price);
        System.out.println(result2);
        
        System.out.println();
    }
    
    private static void demonstrateIntegerFormatting() {
        System.out.println("=== INTEGER FORMATTING ===");
        
        int num = 12345;
        int negative = -789;
        
        // Basic integer formatting
        System.out.println("Basic: " + String.format("%d", num));
        
        // Width and padding
        System.out.println("Width 10: '" + String.format("%10d", num) + "'");
        System.out.println("Left-aligned: '" + String.format("%-10d", num) + "'");
        System.out.println("Zero-padded: '" + String.format("%010d", num) + "'");
        
        // Sign formatting
        System.out.println("Always show sign: " + String.format("%+d", num));
        System.out.println("Space for positive: '" + String.format("% d", num) + "'");
        System.out.println("Negative: " + String.format("%+d", negative));
        
        // Different number bases
        System.out.println("Octal: " + String.format("%o", num));
        System.out.println("Hex (lowercase): " + String.format("%x", num));
        System.out.println("Hex (uppercase): " + String.format("%X", num));
        
        // With prefixes
        System.out.println("Octal with prefix: " + String.format("%#o", num));
        System.out.println("Hex with prefix: " + String.format("%#x", num));
        
        // Thousands separator
        System.out.println("With commas: " + String.format("%,d", 1234567));
        
        System.out.println();
    }
    
    private static void demonstrateFloatFormatting() {
        System.out.println("=== FLOATING POINT FORMATTING ===");
        
        double pi = 3.14159265;
        double big = 12345.6789;
        double small = 0.000123;
        
        // Basic floating point
        System.out.println("Default: " + String.format("%f", pi));
        System.out.println("2 decimals: " + String.format("%.2f", pi));
        System.out.println("0 decimals: " + String.format("%.0f", pi));
        
        // Width and alignment
        System.out.println("Width 10: '" + String.format("%10.2f", pi) + "'");
        System.out.println("Left-aligned: '" + String.format("%-10.2f", pi) + "'");
        System.out.println("Zero-padded: '" + String.format("%010.2f", pi) + "'");
        
        // Scientific notation
        System.out.println("Scientific: " + String.format("%e", big));
        System.out.println("Scientific (caps): " + String.format("%E", big));
        System.out.println("Scientific 2 dec: " + String.format("%.2e", big));
        
        // General format (chooses between %f and %e)
        System.out.println("General large: " + String.format("%g", big));
        System.out.println("General small: " + String.format("%g", small));
        
        // Percentage
        double ratio = 0.75;
        System.out.println("Percentage: " + String.format("%.1%%", ratio * 100));
        
        // With thousands separator
        System.out.println("With commas: " + String.format("%,.2f", big));
        
        System.out.println();
    }
    
    private static void demonstrateStringFormatting() {
        System.out.println("=== STRING FORMATTING ===");
        
        String text = "Hello";
        String longText = "This is a very long string";
        
        // Basic string formatting
        System.out.println("Basic: '" + String.format("%s", text) + "'");
        System.out.println("Uppercase: '" + String.format("%S", text) + "'");
        
        // Width and alignment
        System.out.println("Width 10: '" + String.format("%10s", text) + "'");
        System.out.println("Left-aligned: '" + String.format("%-10s", text) + "'");
        
        // Precision (max characters)
        System.out.println("Max 4 chars: '" + String.format("%.4s", longText) + "'");
        System.out.println("Width 10, max 4: '" + String.format("%10.4s", longText) + "'");
        
        // Character formatting
        char ch = 'A';
        System.out.println("Character: " + String.format("%c", ch));
        System.out.println("ASCII value: " + String.format("%d", (int)ch));
        
        System.out.println();
    }
    
    private static void demonstrateDateTimeFormatting() {
        System.out.println("=== DATE TIME FORMATTING ===");
        
        Date now = new Date();
        Calendar cal = Calendar.getInstance();
        
        // Basic date/time formats
        System.out.println("Full date/time: " + String.format("%tc", now));
        System.out.println("Date only: " + String.format("%tD", now));
        System.out.println("Time only: " + String.format("%tT", now));
        
        // Individual components
        System.out.println("Year: " + String.format("%tY", now));
        System.out.println("Month: " + String.format("%tm", now));
        System.out.println("Day: " + String.format("%td", now));
        System.out.println("Hour (24h): " + String.format("%tH", now));
        System.out.println("Hour (12h): " + String.format("%tI", now));
        System.out.println("AM/PM: " + String.format("%tp", now));
        
        // Custom date format
        String customDate = String.format("%td/%tm/%tY %tH:%tM:%tS", 
                                        now, now, now, now, now, now);
        System.out.println("Custom format: " + customDate);
        
        // Using argument index to avoid repetition
        String betterDate = String.format("%1$td/%1$tm/%1$tY %1$tH:%1$tM:%1$tS", now);
        System.out.println("Better format: " + betterDate);
        
        System.out.println();
    }
    
    private static void demonstrateAdvancedFormatting() {
        System.out.println("=== ADVANCED FORMATTING ===");
        
        // Boolean formatting
        boolean flag = true;
        System.out.println("Boolean: " + String.format("%b", flag));
        System.out.println("Boolean (caps): " + String.format("%B", flag));
        System.out.println("Null as boolean: " + String.format("%b", (Object)null));
        
        // Hash code
        String obj = "test";
        System.out.println("Hash code: " + String.format("%h", obj));
        System.out.println("Hash code (caps): " + String.format("%H", obj));
        
        // Line separator
        String multiline = String.format("Line 1%nLine 2%nLine 3");
        System.out.println("Multi-line:\n" + multiline);
        
        // Literal percent
        System.out.println("Percentage symbol: " + String.format("100%% complete"));
        
        // Complex formatting with multiple flags
        double value = 1234.5678;
        System.out.println("Complex: " + String.format("%+,015.2f", value));
        // Breakdown: %+,015.2f
        // + : always show sign
        // , : thousands separator  
        // 0 : zero padding
        // 15: minimum width
        // .2: 2 decimal places
        // f : floating point
        
        System.out.println();
    }
    
    private static void demonstratePracticalExamples() {
        System.out.println("=== PRACTICAL EXAMPLES ===");
        
        // 1. Financial formatting
        double[] prices = {19.99, 1234.50, 0.99};
        System.out.println("FINANCIAL REPORT:");
        for (int i = 0; i < prices.length; i++) {
            System.out.println(String.format("Item %d: $%,8.2f", i+1, prices[i]));
        }
        
        System.out.println();
        
        // 2. Table formatting
        String[] names = {"Alice", "Bob", "Charlie"};
        int[] ages = {25, 30, 35};
        double[] salaries = {50000, 65000, 80000};
        
        System.out.println("EMPLOYEE TABLE:");
        System.out.println(String.format("%-10s %3s %10s", "Name", "Age", "Salary"));
        System.out.println("-".repeat(25));
        
        for (int i = 0; i < names.length; i++) {
            System.out.println(String.format("%-10s %3d $%,8.0f", 
                                           names[i], ages[i], salaries[i]));
        }
        
        System.out.println();
        
        // 3. Progress indicator
        for (int progress = 0; progress <= 100; progress += 25) {
            String bar = "=".repeat(progress / 5) + " ".repeat(20 - progress / 5);
            System.out.println(String.format("Progress: [%s] %3d%%", bar, progress));
        }
        
        System.out.println();
        
        // 4. Log formatting
        String logEntry = String.format("[%1$tY-%1$tm-%1$td %1$tH:%1$tM:%1$tS] %s: %s",
                                       new Date(), "INFO", "Application started successfully");
        System.out.println("LOG ENTRY:");
        System.out.println(logEntry);
        
        System.out.println();
        
        // 5. Data validation output
        String[] inputs = {"123", "abc", "45.67", ""};
        System.out.println("INPUT VALIDATION:");
        
        for (String input : inputs) {
            boolean isNumeric = input.matches("\\d+(\\.\\d+)?");
            String status = isNumeric ? "VALID" : "INVALID";
            System.out.println(String.format("Input: %-8s | Status: %s", 
                                           "'" + input + "'", status));
        }
    }
}

/**
 * FORMAT SPECIFIER REFERENCE GUIDE
 */
class FormatSpecifierReference {
    
    public static void printReference() {
        System.out.println("\n=== FORMAT SPECIFIER REFERENCE ===");
        
        String reference = """
            
            FORMAT SYNTAX: %[argument_index$][flags][width][.precision]conversion
            
            CONVERSIONS:
            %d, %o, %x, %X  - Integer (decimal, octal, hex lower/upper)
            %f, %e, %E, %g, %G - Floating point (fixed, scientific, general)
            %s, %S          - String (normal, uppercase)
            %c, %C          - Character (normal, uppercase)
            %b, %B          - Boolean (normal, uppercase)
            %h, %H          - Hash code (normal, uppercase)
            %t, %T          - Date/time (various sub-specifiers)
            %n              - Platform-specific line separator
            %%              - Literal percent sign
            
            FLAGS:
            -               - Left-justify
            +               - Always show sign
            (space)         - Leading space for positive numbers
            0               - Zero-pad numbers
            ,               - Use locale-specific grouping separators
            #               - Use alternative format (0x for hex, etc.)
            
            WIDTH:
            number          - Minimum field width
            
            PRECISION:
            .number         - For floating point: decimal places
                             For strings: maximum characters
            
            EXAMPLES:
            %10d           - Integer, minimum width 10, right-aligned
            %-10d          - Integer, minimum width 10, left-aligned
            %010d          - Integer, minimum width 10, zero-padded
            %+d            - Integer, always show sign
            %,d            - Integer with thousands separators
            %.2f           - Float with 2 decimal places
            %10.2f         - Float, width 10, 2 decimal places
            %-10.4s        - String, width 10, max 4 chars, left-aligned
            %tc            - Complete date and time
            %tD            - Date as MM/dd/yy
            %tT            - Time as HH:MM:SS
            """;
        
        System.out.println(reference);
    }
}