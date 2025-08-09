import javax.swing.*;
import javax.swing.Timer;
import java.awt.*;
import java.awt.event.*;
import java.awt.geom.*;
import java.util.*;
import java.util.List;

public class CosmicExplorer extends JFrame {
    private final int WIDTH = 1000;
    private final int HEIGHT = 700;
    private final DrawingPanel drawingPanel;
    private final Timer timer;
    private final List<CelestialBody> celestialBodies = new ArrayList<>();
    private final List<Particle> particles = new ArrayList<>();
    private Point mousePosition = new Point(400, 300);
    private boolean mousePressed = false;
    private float time = 0;

    public CosmicExplorer() {
        setTitle("Cosmic Explorer");
        setSize(WIDTH, HEIGHT);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
        setResizable(false);
        
        drawingPanel = new DrawingPanel();
        add(drawingPanel);
        
        // Create cosmic bodies
        createUniverse();
        
        // Add mouse listeners
        addMouseMotionListener(new MouseAdapter() {
            @Override
            public void mouseMoved(MouseEvent e) {
                mousePosition = e.getPoint();
            }
        });
        
        addMouseListener(new MouseAdapter() {
            @Override
            public void mousePressed(MouseEvent e) {
                mousePressed = true;
                generateParticles(e.getPoint());
            }
            
            @Override
            public void mouseReleased(MouseEvent e) {
                mousePressed = false;
            }
        });
        
        // Animation timer
        timer = new Timer(16, e -> {
            updateUniverse();
            drawingPanel.repaint();
            time += 0.01f;
        });
        timer.start();
        
        // Add custom close button
        addCustomControls();
    }
    
    private void createUniverse() {
        // Create planets
        celestialBodies.add(new Planet(200, 150, 60, new Color(255, 150, 50), 0.2f)); // Sun
        celestialBodies.add(new Planet(400, 250, 25, new Color(100, 180, 255), 0.5f)); // Blue planet
        celestialBodies.add(new Planet(600, 400, 35, new Color(180, 255, 150), -0.3f)); // Green planet
        celestialBodies.add(new Planet(300, 500, 20, new Color(255, 120, 180), 0.4f)); // Pink planet
        
        // Create stars
        for (int i = 0; i < 200; i++) {
            celestialBodies.add(new Star(
                (int)(Math.random() * WIDTH),
                (int)(Math.random() * HEIGHT),
                (float) (Math.random() * 2 + 0.5),
                (float) (Math.random() * 0.05)
            ));
        }
    }
    
    private void updateUniverse() {
        // Update planets
        for (CelestialBody body : celestialBodies) {
            body.update();
        }
        
        // Update particles with gravity
        Iterator<Particle> iter = particles.iterator();
        while (iter.hasNext()) {
            Particle p = iter.next();
            p.update();
            
            // Apply gravity toward mouse
            if (mousePressed) {
                float dx = mousePosition.x - p.x;
                float dy = mousePosition.y - p.y;
                double dist = Math.sqrt(dx*dx + dy*dy);
                if (dist > 5) {
                    p.vx += dx * 0.0001;
                    p.vy += dy * 0.0001;
                }
            }
            
            // Remove dead particles
            if (p.life <= 0) iter.remove();
        }
        
        // Add new particles
        if (mousePressed) {
            generateParticles(mousePosition);
        }
    }
    
    private void generateParticles(Point point) {
        for (int i = 0; i < 5; i++) {
            particles.add(new Particle(
                point.x, 
                point.y,
                (float) (Math.random() - 0.5) * 2,
                (float) (Math.random() - 0.5) * 2,
                new Color(
                    (int)(Math.random() * 55 + 200),
                    (int)(Math.random() * 55 + 200),
                    (int)(Math.random() * 55 + 200),
                    150
                )
            ));
        }
    }
    
    private void addCustomControls() {
        // Create fancy close button
        JButton closeButton = new FancyButton("X");
        closeButton.setBounds(WIDTH - 50, 10, 40, 40);
        closeButton.addActionListener(e -> System.exit(0));
        drawingPanel.add(closeButton);
        
        // Create title label with glow effect
        JLabel title = new JLabel("COSMIC EXPLORER");
        title.setBounds(50, 20, 300, 40);
        title.setFont(new Font("Arial", Font.BOLD, 24));
        title.setForeground(new Color(200, 230, 255));
        drawingPanel.add(title);
    }

    class DrawingPanel extends JPanel {
        public DrawingPanel() {
            setLayout(null);
            setBackground(new Color(10, 10, 30));
        }
        
        @Override
        protected void paintComponent(Graphics g) {
            super.paintComponent(g);
            Graphics2D g2d = (Graphics2D) g;
            g2d.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);
            g2d.setRenderingHint(RenderingHints.KEY_RENDERING, RenderingHints.VALUE_RENDER_QUALITY);
            
            // Draw cosmic nebula background
            drawNebula(g2d);
            
            // Draw celestial bodies
            for (CelestialBody body : celestialBodies) {
                body.draw(g2d);
            }
            
            // Draw particles
            for (Particle particle : particles) {
                particle.draw(g2d);
            }
            
            // Draw interactive cursor effect
            if (mousePressed) {
                drawVortex(g2d, mousePosition.x, mousePosition.y);
            }
            
            // Draw UI elements
            drawUI(g2d);
        }
        
        private void drawNebula(Graphics2D g2d) {
            // Create radial gradient for nebula
            Point2D center = new Point2D.Float(WIDTH/2, HEIGHT/2);
            float radius = Math.max(WIDTH, HEIGHT) / 2 * (0.7f + (float)Math.sin(time) * 0.1f);
            float[] dist = {0.0f, 0.7f, 1.0f};
            Color[] colors = {
                new Color(20, 10, 80, 150),
                new Color(80, 20, 120, 50),
                new Color(10, 10, 30, 0)
            };
            RadialGradientPaint rgp = new RadialGradientPaint(center, radius, dist, colors);
            g2d.setPaint(rgp);
            g2d.fillRect(0, 0, WIDTH, HEIGHT);
        }
        
        private void drawVortex(Graphics2D g2d, int x, int y) {
            // Create vortex effect
            g2d.setComposite(AlphaComposite.getInstance(AlphaComposite.SRC_OVER, 0.7f));
            for (int i = 0; i < 5; i++) {
                float size = 80 + i * 30;
                g2d.setColor(new Color(150, 200, 255, 100 - i * 20));
                g2d.setStroke(new BasicStroke(2));
                g2d.drawOval((int)(x - size/2), (int)(y - size/2), (int)size, (int)size);
            }
            g2d.setComposite(AlphaComposite.getInstance(AlphaComposite.SRC_OVER, 1f));
            
            // Draw center glow
            RadialGradientPaint centerGlow = new RadialGradientPaint(
                new Point2D.Float(x, y), 40,
                new float[]{0f, 1f},
                new Color[]{new Color(200, 230, 255, 150), new Color(200, 230, 255, 0)}
            );
            g2d.setPaint(centerGlow);
            g2d.fillOval(x - 40, y - 40, 80, 80);
        }
        
        private void drawUI(Graphics2D g2d) {
            // Draw info panel with glass effect
            g2d.setComposite(AlphaComposite.getInstance(AlphaComposite.SRC_OVER, 0.7f));
            g2d.setColor(new Color(30, 30, 60, 200));
            g2d.fillRoundRect(30, HEIGHT - 100, 300, 70, 20, 20);
            
            // Draw border
            g2d.setStroke(new BasicStroke(2));
            g2d.setColor(new Color(150, 180, 255));
            g2d.drawRoundRect(30, HEIGHT - 100, 300, 70, 20, 20);
            
            // Draw text
            g2d.setComposite(AlphaComposite.getInstance(AlphaComposite.SRC_OVER, 1f));
            g2d.setColor(Color.WHITE);
            g2d.setFont(new Font("Arial", Font.PLAIN, 16));
            g2d.drawString("Particles: " + particles.size(), 50, HEIGHT - 75);
            g2d.drawString("Click and drag to create gravity vortex", 50, HEIGHT - 50);
        }
    }
    
    // Celestial body base class
    abstract class CelestialBody {
        float x, y;
        float rotation;
        
        abstract void update();
        abstract void draw(Graphics2D g2d);
    }
    
    // Planet class
    class Planet extends CelestialBody {
        float radius;
        Color color;
        float rotationSpeed;
        float orbitRadius;
        float orbitAngle;
        float orbitSpeed;
        
        public Planet(float x, float y, float radius, Color color, float rotationSpeed) {
            this.x = x;
            this.y = y;
            this.radius = radius;
            this.color = color;
            this.rotationSpeed = rotationSpeed;
            this.orbitRadius = radius * 3;
            this.orbitAngle = (float) (Math.random() * Math.PI * 2);
            this.orbitSpeed = rotationSpeed * 0.1f;
        }
        
        @Override
        void update() {
            rotation += rotationSpeed;
            orbitAngle += orbitSpeed;
            
            // Simple orbit effect
            x = x + (float) Math.cos(orbitAngle) * 0.5f;
            y = y + (float) Math.sin(orbitAngle) * 0.5f;
        }
        
        @Override
        void draw(Graphics2D g2d) {
            // Draw glow
            RadialGradientPaint glow = new RadialGradientPaint(
                new Point2D.Float(x, y), radius * 2,
                new float[]{0f, 1f},
                new Color[]{new Color(color.getRed(), color.getGreen(), color.getBlue(), 100), 
                           new Color(color.getRed(), color.getGreen(), color.getBlue(), 0)}
            );
            g2d.setPaint(glow);
            g2d.fillOval((int)(x - radius * 2), (int)(y - radius * 2), (int)(radius * 4), (int)(radius * 4));
            
            // Draw planet
            g2d.setColor(color);
            g2d.fillOval((int)(x - radius), (int)(y - radius), (int)(radius * 2), (int)(radius * 2));
            
            // Draw rings for larger planets
            if (radius > 25) {
                g2d.setStroke(new BasicStroke(3));
                g2d.setColor(new Color(200, 200, 220, 150));
                g2d.rotate(rotation, x, y);
                g2d.drawOval((int)(x - radius * 1.5), (int)(y - radius * 0.5), (int)(radius * 3), (int)(radius));
                g2d.rotate(-rotation, x, y);
            }
            
            // Draw craters
            g2d.setColor(color.darker());
            for (int i = 0; i < 5; i++) {
                float angle = (float) (Math.PI * 2 / 5 * i + rotation);
                float cr = radius * 0.2f;
                float cx = x + (float) Math.cos(angle) * radius * 0.7f;
                float cy = y + (float) Math.sin(angle) * radius * 0.7f;
                g2d.fillOval((int)(cx - cr), (int)(cy - cr), (int)(cr * 2), (int)(cr * 2));
            }
        }
    }
    
    // Star class
    class Star extends CelestialBody {
        float size;
        float pulseSpeed;
        float pulse;
        
        public Star(float x, float y, float size, float pulseSpeed) {
            this.x = x;
            this.y = y;
            this.size = size;
            this.pulseSpeed = pulseSpeed;
            this.pulse = (float) Math.random();
        }
        
        @Override
        void update() {
            pulse = (float) ((Math.sin(time * pulseSpeed) + 1) / 2);
        }
        
        @Override
        void draw(Graphics2D g2d) {
            float currentSize = size * (0.8f + pulse * 0.4f);
            g2d.setColor(new Color(255, 255, 200, (int)(100 + pulse * 155)));
            g2d.fillOval((int)(x - currentSize), (int)(y - currentSize), 
                         (int)(currentSize * 2), (int)(currentSize * 2));
            
            // Draw star rays
            if (pulse > 0.7) {
                g2d.setStroke(new BasicStroke(1.5f));
                for (int i = 0; i < 8; i++) {
                    double angle = Math.PI / 4 * i;
                    float length = currentSize * 3;
                    float endX = x + (float) (Math.cos(angle) * length);
                    float endY = y + (float) (Math.sin(angle) * length);
                    g2d.drawLine((int)x, (int)y, (int)endX, (int)endY);
                }
            }
        }
    }
    
    // Particle class
    class Particle {
        float x, y;
        float vx, vy;
        Color color;
        float life = 1.0f; // 1.0 = full life, 0.0 = dead
        float size;
        
        public Particle(float x, float y, float vx, float vy, Color color) {
            this.x = x;
            this.y = y;
            this.vx = vx;
            this.vy = vy;
            this.color = color;
            this.size = (float) (Math.random() * 4 + 2);
        }
        
        void update() {
            x += vx;
            y += vy;
            
            // Apply friction
            vx *= 0.98;
            vy *= 0.98;
            
            // Gradually fade out
            life -= 0.005f;
            
            // Bounce off edges
            if (x < 0 || x > WIDTH) vx = -vx;
            if (y < 0 || y > HEIGHT) vy = -vy;
        }
        
        void draw(Graphics2D g2d) {
            float alpha = life * 0.8f;
            Color particleColor = new Color(
                color.getRed(),
                color.getGreen(),
                color.getBlue(),
                (int)(alpha * 255)
            );
            
            g2d.setColor(particleColor);
            g2d.fillOval((int)(x - size), (int)(y - size), (int)(size * 2), (int)(size * 2));
            
            // Draw glow
            RadialGradientPaint glow = new RadialGradientPaint(
                new Point2D.Float(x, y), size * 3,
                new float[]{0f, 1f},
                new Color[]{particleColor, new Color(particleColor.getRed(), 
                                                   particleColor.getGreen(), 
                                                   particleColor.getBlue(), 0)}
            );
            g2d.setPaint(glow);
            g2d.fillOval((int)(x - size * 3), (int)(y - size * 3), 
                         (int)(size * 6), (int)(size * 6));
        }
    }
    
    // Custom styled button
    class FancyButton extends JButton {
        private boolean hovered = false;
        
        public FancyButton(String text) {
            super(text);
            setContentAreaFilled(false);
            setBorderPainted(false);
            setFocusPainted(false);
            setFont(new Font("Arial", Font.BOLD, 18));
            
            addMouseListener(new MouseAdapter() {
                @Override
                public void mouseEntered(MouseEvent e) {
                    hovered = true;
                    repaint();
                }
                
                @Override
                public void mouseExited(MouseEvent e) {
                    hovered = false;
                    repaint();
                }
            });
        }
        
        @Override
        protected void paintComponent(Graphics g) {
            Graphics2D g2d = (Graphics2D) g.create();
            g2d.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);
            
            // Create glass-like button
            int width = getWidth();
            int height = getHeight();
            
            // Background gradient
            GradientPaint bgGradient = new GradientPaint(
                0, 0, new Color(80, 100, 200, 200),
                0, height, new Color(40, 60, 150, 200)
            );
            g2d.setPaint(bgGradient);
            g2d.fillRoundRect(0, 0, width, height, 20, 20);
            
            // Glass highlight
            GradientPaint glassGradient = new GradientPaint(
                0, 0, new Color(255, 255, 255, hovered ? 120 : 80),
                0, height/2, new Color(255, 255, 255, 20)
            );
            g2d.setPaint(glassGradient);
            g2d.fillRoundRect(2, 2, width - 4, height/2, 18, 18);
            
            // Border
            g2d.setStroke(new BasicStroke(2f));
            g2d.setColor(new Color(180, 200, 255, 200));
            g2d.drawRoundRect(1, 1, width - 2, height - 2, 18, 18);
            
            // Text
            g2d.setColor(Color.WHITE);
            FontMetrics fm = g2d.getFontMetrics();
            Rectangle r = getBounds();
            int textX = (r.width - fm.stringWidth(getText())) / 2;
            int textY = (r.height - fm.getHeight()) / 2 + fm.getAscent();
            g2d.drawString(getText(), textX, textY);
            
            // Glow effect on hover
            if (hovered) {
                g2d.setComposite(AlphaComposite.getInstance(AlphaComposite.SRC_OVER, 0.4f));
                g2d.setColor(new Color(200, 220, 255));
                g2d.fillRoundRect(0, 0, width, height, 20, 20);
            }
            
            g2d.dispose();
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            CosmicExplorer explorer = new CosmicExplorer();
            explorer.setVisible(true);
        });
    }
}
