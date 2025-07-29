static class Point {
    double x, y;
    String id;

    Point(double x, double y, String id) {
        this.x = x;
        this.y = y;
        this.id = id;
    }
}

static double distance(Point a, Point b) {
    return Math.sqrt(Math.pow(a.x - b.x, 2) + Math.pow(a.y - b.y, 2));
}

static Point[] findCloseTriple(List<Point> Px, List<Point> Py) {
    int n = Px.size();
    if (n <= 3) {
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                for (int k = j + 1; k < n; k++) {
                    if (distance(Px.get(i), Px.get(j)) <= 1 &&
                        distance(Px.get(i), Px.get(k)) <= 1 &&
                        distance(Px.get(j), Px.get(k)) <= 1) {
                        return new Point[]{Px.get(i), Px.get(j), Px.get(k)};
                    }
                }
            }
        }
        return null;
    }

    int mid = n / 2;
    Point midPoint = Px.get(mid);

    List<Point> Qx = Px.subList(0, mid);
    List<Point> Rx = Px.subList(mid, n);

    List<Point> Qy = new ArrayList<>();
    List<Point> Ry = new ArrayList<>();
    for (Point p : Py) {
        if (p.x <= midPoint.x) Qy.add(p);
        else Ry.add(p);
    }

    Point[] left = findCloseTriple(Qx, Qy);
    if (left != null) return left;

    Point[] right = findCloseTriple(Rx, Ry);
    if (right != null) return right;

    List<Point> strip = new ArrayList<>();
    for (Point p : Py) {
        if (Math.abs(p.x - midPoint.x) <= 1)
            strip.add(p);
    }

    for (int i = 0; i < strip.size(); i++) {
        List<Point> nearby = new ArrayList<>();
        for (int j = i + 1; j < strip.size() && (strip.get(j).y - strip.get(i).y) <= 1; j++) {
            if (distance(strip.get(i), strip.get(j)) <= 1) {
                nearby.add(strip.get(j));
            }
        }

        for (int a = 0; a < nearby.size(); a++) {
            for (int b = a + 1; b < nearby.size(); b++) {
                if (distance(nearby.get(a), nearby.get(b)) <= 1) {
                    return new Point[]{strip.get(i), nearby.get(a), nearby.get(b)};
                }
            }
        }
    }

    return null;
}

public static void main(String[] args) {
    List<Point> points = new ArrayList<>();
    points.add(new Point(0.0, 0.0, "A"));
    points.add(new Point(0.5, 0.4, "B"));
    points.add(new Point(0.3, 0.8, "C"));  // Close to both A and B

    points.add(new Point(2.0, 2.0, "D"));
    points.add(new Point(3.5, 0.0, "E"));
    points.add(new Point(4.0, 1.0, "F"));

    List<Point> Lx = new ArrayList<>(points);
    List<Point> Ly = new ArrayList<>(points);

    Lx.sort(Comparator.comparingDouble(p -> p.x));
    Ly.sort(Comparator.comparingDouble(p -> p.y));

    Point[] result = findCloseTriple(Lx, Ly);
    if (result != null) {
        System.out.println("Close triple found:");
        for (Point p : result) {
            System.out.println(p.id + " at (" + p.x + ", " + p.y + ")");
        }
    } else {
        System.out.println("No triple found within distance 1.");
    }
}

