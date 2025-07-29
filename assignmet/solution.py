def find_three_close_points(Lx, Ly):
    """
    Find three points that are all within Euclidean distance 1 from each other.
    Uses divide-and-conquer approach.
    
    Args:
        Lx: List of points sorted by x-coordinate
        Ly: List of points sorted by y-coordinate
    
    Returns:
        Tuple of three points if found, None otherwise
    """
    
    def distance(p1, p2):
        return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5
    
    def find_three_close_brute_force(points):
        """Brute force for small inputs"""
        n = len(points)
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if (distance(points[i], points[j]) <= 1 and 
                        distance(points[i], points[k]) <= 1 and 
                        distance(points[j], points[k]) <= 1):
                        return (points[i], points[j], points[k])
        return None
    
    def find_three_close_rec(px, py):
        n = len(px)
        
        # Base case: use brute force for small inputs
        if n <= 10:
            return find_three_close_brute_force(px)
        
        # Divide
        mid = n // 2
        midpoint = px[mid]
        
        pyl = [point for point in py if point[0] <= midpoint[0]]
        pyr = [point for point in py if point[0] > midpoint[0]]
        
        # Conquer
        left_result = find_three_close_rec(px[:mid], pyl)
        if left_result:
            return left_result
            
        right_result = find_three_close_rec(px[mid:], pyr)
        if right_result:
            return right_result
        
        # Combine: Check for triangles crossing the dividing line
        # Create strip of points within distance 1 of the dividing line
        strip = []
        for point in py:
            if abs(point[0] - midpoint[0]) <= 1:
                strip.append(point)
        
        # Check all combinations of 3 points in the strip
        # Since strip is sorted by y-coordinate, we can optimize
        strip_len = len(strip)
        for i in range(strip_len):
            for j in range(i + 1, strip_len):
                # Early termination: if y-distance > 1, no need to check further
                if strip[j][1] - strip[i][1] > 1:
                    break
                for k in range(j + 1, strip_len):
                    if strip[k][1] - strip[i][1] > 1:
                        break
                    
                    # Check if all three points are within distance 1
                    if (distance(strip[i], strip[j]) <= 1 and 
                        distance(strip[i], strip[k]) <= 1 and 
                        distance(strip[j], strip[k]) <= 1):
                        return (strip[i], strip[j], strip[k])
        
        return None
    
    return find_three_close_rec(Lx, Ly)

# Example usage
if __name__ == "__main__":
    # Test case 1: Three points forming a small triangle
    points1 = [(0, 0), (0.5, 0), (0.25, 0.4)]
    Lx1 = sorted(points1, key=lambda p: p[0])
    Ly1 = sorted(points1, key=lambda p: p[1])
    
    result1 = find_three_close_points(Lx1, Ly1)
    print("Test 1 - Three close points:", result1)
    
    # Test case 2: No three points all within distance 1
    points2 = [(0, 0), (2, 0), (1, 2)]
    Lx2 = sorted(points2, key=lambda p: p[0])
    Ly2 = sorted(points2, key=lambda p: p[1])
    
    result2 = find_three_close_points(Lx2, Ly2)
    print("Test 2 - No three close points:", result2)