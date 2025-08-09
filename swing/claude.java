import javax.swing.*;
import javax.swing.border.EmptyBorder;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.awt.geom.RoundRectangle2D;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.Random;

public class FancyDigitalDashboard extends JFrame {
    private static final Color DARK_BG = new Color(20, 25, 40);
    private static final Color CARD_BG = new Color(40, 45, 65);
    private static final Color ACCENT_BLUE = new Color(64, 156, 255);
    private static final Color ACCENT_GREEN = new Color(46, 204, 113);
    private static final Color ACCENT_ORANGE = new Color(255, 159, 67);
    private static final Color TEXT_PRIMARY = new Color(236, 240, 241);
    private static final Color TEXT_SECONDARY = new Color(149, 165, 166);
    
    private Timer clockTimer, animationTimer, particleTimer;
    private JLabel timeLabel, dateLabel;
    private AnimatedProgressBar cpuBar, memoryBar, diskBar;
    private ParticlePanel particlePanel;
    private int animationFrame = 0;
    private Random random = new Random();
    
    public FancyDigitalDashboard() {
        initializeFrame();
        createComponents();
        startAnimations();
    }
    
    private void initializeFrame() {
        setTitle("Digital Dashboard v2.0");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(1200, 800);
        setLocationRelativeTo(null);
        setBackground(DARK_BG);
        
        // Custom window decoration
        setUndecorated(true);
        setShape(new RoundRectangle2D.Double(0, 0, 1200, 800, 20, 20));
        
        // Add drag functionality
        addMouseMotionListener(new MouseAdapter() {
            Point lastPoint;
            public void mouseDragged(MouseEvent e) {
                Point currentPoint = e.getLocationOnScreen();
                if (lastPoint != null) {
                    setLocation(currentPoint.x - lastPoint.x + getLocation().x,
                              currentPoint.y - lastPoint.y + getLocation().y);
                }
                lastPoint = currentPoint;
            }
            public void mouseMoved(MouseEvent e) {
                lastPoint = e.getLocationOnScreen();
            }
        });
    }
    
    private void createComponents() {
        setLayout(new BorderLayout());
        
        // Header Panel
        JPanel headerPanel = createHeaderPanel();
        add(headerPanel, BorderLayout.NORTH);
        
        // Main Content
        JPanel mainPanel = new JPanel(new GridLayout(2, 3, 20, 20));
        mainPanel.setBackground(DARK_BG);
        mainPanel.setBorder(new EmptyBorder(20, 20, 20, 20));
        
        // Add cards
        mainPanel.add(createTimeCard());
        mainPanel.add(createSystemStatsCard());
        mainPanel.add(createWeatherCard());
        
        // Particle background panel
        particlePanel = new ParticlePanel();
        mainPanel.add(particlePanel);
        
        mainPanel.add(createQuickActionsCard());
        mainPanel.add(createNetworkCard());
        
        add(mainPanel, BorderLayout.CENTER);
    }
    
    private JPanel createHeaderPanel() {
        JPanel header = new JPanel(new BorderLayout());
        header.setBackground(CARD_BG);
        header.setBorder(new EmptyBorder(15, 20, 15, 20));
        
        JLabel titleLabel = new JLabel("Digital Dashboard");
        titleLabel.setFont(new Font("Segoe UI", Font.BOLD, 24));
        titleLabel.setForeground(TEXT_PRIMARY);
        
        JButton closeBtn = createStyledButton("✕", ACCENT_ORANGE);
        closeBtn.addActionListener(e -> System.exit(0));
        
        JButton minimizeBtn = createStyledButton("–", ACCENT_BLUE);
        minimizeBtn.addActionListener(e -> setState(JFrame.ICONIFIED));
        
        JPanel buttonPanel = new JPanel(new FlowLayout(FlowLayout.RIGHT, 5, 0));
        buttonPanel.setBackground(CARD_BG);
        buttonPanel.add(minimizeBtn);
        buttonPanel.add(closeBtn);
        
        header.add(titleLabel, BorderLayout.WEST);
        header.add(buttonPanel, BorderLayout.EAST);
        
        return header;
    }
    
    private JPanel createTimeCard() {
        JPanel card = createCard("Current Time");
        card.setLayout(new BoxLayout(card, BoxLayout.Y_AXIS));
        
        timeLabel = new JLabel();
        timeLabel.setFont(new Font("Segoe UI", Font.BOLD, 36));
        timeLabel.setForeground(ACCENT_BLUE);
        timeLabel.setAlignmentX(Component.CENTER_ALIGNMENT);
        
        dateLabel = new JLabel();
        dateLabel.setFont(new Font("Segoe UI", Font.PLAIN, 16));
        dateLabel.setForeground(TEXT_SECONDARY);
        dateLabel.setAlignmentX(Component.CENTER_ALIGNMENT);
        
        card.add(Box.createVerticalGlue());
        card.add(timeLabel);
        card.add(Box.createVerticalStrut(10));
        card.add(dateLabel);
        card.add(Box.createVerticalGlue());
        
        return card;
    }
    
    private JPanel createSystemStatsCard() {
        JPanel card = createCard("System Performance");
        card.setLayout(new BoxLayout(card, BoxLayout.Y_AXIS));
        
        cpuBar = new AnimatedProgressBar("CPU Usage", ACCENT_BLUE);
        memoryBar = new AnimatedProgressBar("Memory", ACCENT_GREEN);
        diskBar = new AnimatedProgressBar("Disk I/O", ACCENT_ORANGE);
        
        card.add(Box.createVerticalStrut(10));
        card.add(cpuBar);
        card.add(Box.createVerticalStrut(15));
        card.add(memoryBar);
        card.add(Box.createVerticalStrut(15));
        card.add(diskBar);
        card.add(Box.createVerticalGlue());
        
        return card;
    }
    
    private JPanel createWeatherCard() {
        JPanel card = createCard("Weather Info");
        card.setLayout(new BoxLayout(card, BoxLayout.Y_AXIS));
        
        JLabel weatherIcon = new JLabel("☀", SwingConstants.CENTER);
        weatherIcon.setFont(new Font("Segoe UI", Font.PLAIN, 48));
        weatherIcon.setForeground(ACCENT_ORANGE);
        
        JLabel tempLabel = new JLabel("24°C", SwingConstants.CENTER);
        tempLabel.setFont(new Font("Segoe UI", Font.BOLD, 28));
        tempLabel.setForeground(TEXT_PRIMARY);
        
        JLabel conditionLabel = new JLabel("Sunny", SwingConstants.CENTER);
        conditionLabel.setFont(new Font("Segoe UI", Font.PLAIN, 16));
        conditionLabel.setForeground(TEXT_SECONDARY);
        
        card.add(Box.createVerticalGlue());
        card.add(weatherIcon);
        card.add(Box.createVerticalStrut(10));
        card.add(tempLabel);
        card.add(Box.createVerticalStrut(5));
        card.add(conditionLabel);
        card.add(Box.createVerticalGlue());
        
        return card;
    }
    
    private JPanel createQuickActionsCard() {
        JPanel card = createCard("Quick Actions");
        card.setLayout(new GridLayout(2, 2, 10, 10));
        
        JButton btn1 = createStyledButton("📊 Analytics", ACCENT_BLUE);
        JButton btn2 = createStyledButton("⚙ Settings", ACCENT_GREEN);
        JButton btn3 = createStyledButton("📁 Files", ACCENT_ORANGE);
        JButton btn4 = createStyledButton("🔄 Refresh", ACCENT_BLUE);
        
        btn1.addActionListener(e -> showNotification("Analytics opened!"));
        btn2.addActionListener(e -> showNotification("Settings panel activated!"));
        btn3.addActionListener(e -> showNotification("File manager launched!"));
        btn4.addActionListener(e -> refreshData());
        
        card.add(btn1);
        card.add(btn2);
        card.add(btn3);
        card.add(btn4);
        
        return card;
    }
    
    private JPanel createNetworkCard() {
        JPanel card = createCard("Network Status");
        card.setLayout(new BoxLayout(card, BoxLayout.Y_AXIS));
        
        JLabel statusIcon = new JLabel("📡", SwingConstants.CENTER);
        statusIcon.setFont(new Font("Segoe UI", Font.PLAIN, 36));
        
        JLabel statusLabel = new JLabel("Connected", SwingConstants.CENTER);
        statusLabel.setFont(new Font("Segoe UI", Font.BOLD, 20));
        statusLabel.setForeground(ACCENT_GREEN);
        
        JLabel speedLabel = new JLabel("↓ 45.2 Mbps ↑ 12.1 Mbps", SwingConstants.CENTER);
        speedLabel.setFont(new Font("Segoe UI", Font.PLAIN, 14));
        speedLabel.setForeground(TEXT_SECONDARY);
        
        card.add(Box.createVerticalGlue());
        card.add(statusIcon);
        card.add(Box.createVerticalStrut(10));
        card.add(statusLabel);
        card.add(Box.createVerticalStrut(5));
        card.add(speedLabel);
        card.add(Box.createVerticalGlue());
        
        return card;
    }
    
    private JPanel createCard(String title) {
        JPanel card = new JPanel();
        card.setBackground(CARD_BG);
        card.setBorder(BorderFactory.createCompoundBorder(
            BorderFactory.createLineBorder(new Color(60, 65, 85), 1),
            new EmptyBorder(20, 20, 20, 20)
        ));
        
        // Add title if provided
        if (title != null && !title.isEmpty()) {
            card.setLayout(new BorderLayout());
            JLabel titleLabel = new JLabel(title);
            titleLabel.setFont(new Font("Segoe UI", Font.BOLD, 14));
            titleLabel.setForeground(TEXT_SECONDARY);
            titleLabel.setBorder(new EmptyBorder(0, 0, 15, 0));
            card.add(titleLabel, BorderLayout.NORTH);
            
            JPanel content = new JPanel();
            content.setBackground(CARD_BG);
            card.add(content, BorderLayout.CENTER);
            return content;
        }
        
        return card;
    }
    
    private JButton createStyledButton(String text, Color color) {
        JButton button = new JButton(text) {
            @Override
            protected void paintComponent(Graphics g) {
                Graphics2D g2 = (Graphics2D) g.create();
                g2.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);
                
                if (getModel().isPressed()) {
                    g2.setColor(color.darker());
                } else if (getModel().isRollover()) {
                    g2.setColor(color.brighter());
                } else {
                    g2.setColor(color);
                }
                
                g2.fillRoundRect(0, 0, getWidth(), getHeight(), 8, 8);
                
                g2.setColor(TEXT_PRIMARY);
                FontMetrics fm = g2.getFontMetrics();
                int x = (getWidth() - fm.stringWidth(getText())) / 2;
                int y = (getHeight() + fm.getAscent()) / 2 - 2;
                g2.drawString(getText(), x, y);
                
                g2.dispose();
            }
        };
        
        button.setPreferredSize(new Dimension(120, 40));
        button.setFont(new Font("Segoe UI", Font.BOLD, 12));
        button.setFocusPainted(false);
        button.setBorderPainted(false);
        button.setContentAreaFilled(false);
        button.setCursor(new Cursor(Cursor.HAND_CURSOR));
        
        return button;
    }
    
    private void startAnimations() {
        // Clock timer
        clockTimer = new Timer(1000, e -> updateTime());
        clockTimer.start();
        updateTime();
        
        // Animation timer for progress bars
        animationTimer = new Timer(100, e -> {
            animationFrame++;
            cpuBar.setValue(30 + (int)(20 * Math.sin(animationFrame * 0.1)));
            memoryBar.setValue(45 + (int)(15 * Math.cos(animationFrame * 0.08)));
            diskBar.setValue(20 + (int)(25 * Math.sin(animationFrame * 0.12)));
        });
        animationTimer.start();
        
        // Particle animation timer
        particleTimer = new Timer(50, e -> {
            if (particlePanel != null) {
                particlePanel.repaint();
            }
        });
        particleTimer.start();
    }
    
    private void updateTime() {
        LocalDateTime now = LocalDateTime.now();
        timeLabel.setText(now.format(DateTimeFormatter.ofPattern("HH:mm:ss")));
        dateLabel.setText(now.format(DateTimeFormatter.ofPattern("EEEE, MMMM d, yyyy")));
    }
    
    private void refreshData() {
        showNotification("Data refreshed successfully!");
        // Simulate data refresh with random values
        SwingUtilities.invokeLater(() -> {
            cpuBar.setValue(random.nextInt(80) + 10);
            memoryBar.setValue(random.nextInt(60) + 20);
            diskBar.setValue(random.nextInt(70) + 5);
        });
    }
    
    private void showNotification(String message) {
        JOptionPane.showMessageDialog(this, message, "Notification", 
                                    JOptionPane.INFORMATION_MESSAGE);
    }
    
    // Custom animated progress bar
    class AnimatedProgressBar extends JPanel {
        private String label;
        private Color color;
        private int value = 0;
        private int targetValue = 0;
        
        public AnimatedProgressBar(String label, Color color) {
            this.label = label;
            this.color = color;
            setPreferredSize(new Dimension(200, 40));
            setBackground(CARD_BG);
        }
        
        public void setValue(int value) {
            this.targetValue = Math.max(0, Math.min(100, value));
            // Smooth animation to target value
            Timer smoothTimer = new Timer(20, new ActionListener() {
                public void actionPerformed(ActionEvent e) {
                    if (AnimatedProgressBar.this.value < targetValue) {
                        AnimatedProgressBar.this.value++;
                    } else if (AnimatedProgressBar.this.value > targetValue) {
                        AnimatedProgressBar.this.value--;
                    } else {
                        ((Timer)e.getSource()).stop();
                    }
                    repaint();
                }
            });
            smoothTimer.start();
        }
        
        @Override
        protected void paintComponent(Graphics g) {
            super.paintComponent(g);
            Graphics2D g2 = (Graphics2D) g.create();
            g2.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);
            
            // Draw label
            g2.setColor(TEXT_PRIMARY);
            g2.setFont(new Font("Segoe UI", Font.BOLD, 12));
            g2.drawString(label, 0, 15);
            
            // Draw progress bar background
            g2.setColor(new Color(60, 65, 85));
            g2.fillRoundRect(0, 20, getWidth(), 15, 8, 8);
            
            // Draw progress bar fill
            int fillWidth = (int) ((double) value / 100 * getWidth());
            g2.setColor(color);
            g2.fillRoundRect(0, 20, fillWidth, 15, 8, 8);
            
            // Draw percentage text
            g2.setColor(TEXT_SECONDARY);
            g2.setFont(new Font("Segoe UI", Font.PLAIN, 10));
            String percentage = value + "%";
            FontMetrics fm = g2.getFontMetrics();
            int textX = getWidth() - fm.stringWidth(percentage);
            g2.drawString(percentage, textX, 12);
            
            g2.dispose();
        }
    }
    
    // Particle animation panel
    class ParticlePanel extends JPanel {
        private java.util.List<Particle> particles;
        
        public ParticlePanel() {
            setBackground(CARD_BG);
            particles = new java.util.ArrayList<>();
            
            // Initialize particles
            for (int i = 0; i < 20; i++) {
                particles.add(new Particle());
            }
        }
        
        @Override
        protected void paintComponent(Graphics g) {
            super.paintComponent(g);
            Graphics2D g2 = (Graphics2D) g.create();
            g2.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);
            
            // Update and draw particles
            for (Particle p : particles) {
                p.update(getWidth(), getHeight());
                p.draw(g2);
            }
            
            g2.dispose();
        }
        
        class Particle {
            private double x, y, vx, vy;
            private Color color;
            private int size;
            
            public Particle() {
                reset();
            }
            
            private void reset() {
                x = random.nextDouble() * 300;
                y = random.nextDouble() * 200;
                vx = (random.nextDouble() - 0.5) * 2;
                vy = (random.nextDouble() - 0.5) * 2;
                size = random.nextInt(3) + 1;
                
                Color[] colors = {ACCENT_BLUE, ACCENT_GREEN, ACCENT_ORANGE};
                color = new Color(colors[random.nextInt(colors.length)].getRed(),
                                colors[random.nextInt(colors.length)].getGreen(),
                                colors[random.nextInt(colors.length)].getBlue(), 100);
            }
            
            public void update(int width, int height) {
                x += vx;
                y += vy;
                
                if (x < 0 || x > width || y < 0 || y > height) {
                    reset();
                }
            }
            
            public void draw(Graphics2D g2) {
                g2.setColor(color);
                g2.fillOval((int)x, (int)y, size, size);
            }
        }
    }
    
    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            try {
                // Set system look and feel
                for (UIManager.LookAndFeelInfo info : UIManager.getInstalledLookAndFeels()) {
                    if ("Nimbus".equals(info.getName())) {
                        UIManager.setLookAndFeel(info.getClassName());
                        break;
                    }
                }
            } catch (Exception e) {
                // Use default look and feel if Nimbus is not available
            }
            
            new FancyDigitalDashboard().setVisible(true);
        });
    }
}
