
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.time.LocalTime;
import java.time.format.DateTimeFormatter;

public class FancyDashboard extends JFrame {
    private JLabel clockLabel;
    private JPanel buttonPanel;
    private Timer clockTimer;
    private Color[] colors = {new Color(60, 90, 153), new Color(45, 180, 145), new Color(255, 85, 85), new Color(255, 195, 0)};
    private int colorIndex = 0;

    public FancyDashboard() {
        setTitle("Fancy Java Swing Dashboard ✨");
        setSize(600, 400);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
        setLayout(new BorderLayout());
        getContentPane().setBackground(new Color(30, 30, 30));

        // Title label
        JLabel titleLabel = new JLabel("🌟 Welcome to Fancy Dashboard");
        titleLabel.setForeground(Color.WHITE);
        titleLabel.setFont(new Font("Segoe UI", Font.BOLD, 24));
        titleLabel.setHorizontalAlignment(SwingConstants.CENTER);
        add(titleLabel, BorderLayout.NORTH);

        // Clock Label
        clockLabel = new JLabel();
        clockLabel.setForeground(Color.CYAN);
        clockLabel.setFont(new Font("Consolas", Font.PLAIN, 20));
        clockLabel.setHorizontalAlignment(SwingConstants.CENTER);
        add(clockLabel, BorderLayout.SOUTH);

        // Panel with animated buttons
        buttonPanel = new JPanel();
        buttonPanel.setBackground(new Color(40, 40, 40));
        buttonPanel.setLayout(new GridLayout(2, 2, 20, 20));
        buttonPanel.setBorder(BorderFactory.createEmptyBorder(20, 40, 20, 40));

        addButton("Analytics", "View stats and performance metrics 📊");
        addButton("Settings", "Configure your preferences ⚙️");
        addButton("Notifications", "Check alerts and messages 🔔");
        addButton("Exit", "Close the dashboard ❌", e -> System.exit(0));

        add(buttonPanel, BorderLayout.CENTER);

        // Start the live clock
        startClock();

        // Background animation
        Timer colorCycle = new Timer(2500, e -> {
            buttonPanel.setBackground(colors[colorIndex % colors.length]);
            colorIndex++;
        });
        colorCycle.start();
    }

    private void startClock() {
        clockTimer = new Timer(1000, e -> {
            String time = LocalTime.now().format(DateTimeFormatter.ofPattern("HH:mm:ss"));
            clockLabel.setText("⏰ Current Time: " + time);
        });
        clockTimer.start();
    }

    private void addButton(String name, String tooltip) {
        addButton(name, tooltip, null);
    }

    private void addButton(String name, String tooltip, ActionListener extraAction) {
        JButton button = new JButton(name);
        button.setToolTipText(tooltip);
        button.setFont(new Font("Segoe UI", Font.PLAIN, 16));
        button.setFocusPainted(false);
        button.setBackground(new Color(50, 50, 50));
        button.setForeground(Color.WHITE);
        button.setBorder(BorderFactory.createLineBorder(Color.GRAY, 1));
        button.setCursor(new Cursor(Cursor.HAND_CURSOR));

        button.addMouseListener(new MouseAdapter() {
            @Override
            public void mouseEntered(MouseEvent e) {
                button.setBackground(new Color(100, 100, 200));
            }

            @Override
            public void mouseExited(MouseEvent e) {
                button.setBackground(new Color(50, 50, 50));
            }
        });

        if (extraAction != null) button.addActionListener(extraAction);
        else button.addActionListener(e -> JOptionPane.showMessageDialog(this,
                "You clicked on " + name + "!", name + " Clicked",
                JOptionPane.INFORMATION_MESSAGE));

        buttonPanel.add(button);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            FancyDashboard dashboard = new FancyDashboard();
            dashboard.setVisible(true);
        });
    }
}
