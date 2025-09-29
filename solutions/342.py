
import math

def main():
    with open('INPUT.TXT', 'r') as f:
        n = int(f.readline().strip())
        points = []
        for i in range(n):
            x, y = map(int, f.readline().split())
            points.append((x, y))
    
    def distance(p1, p2):
        return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)
    
    def line_intersection(line1, line2):
        x1, y1 = line1[0]
        x2, y2 = line1[1]
        x3, y3 = line2[0]
        x4, y4 = line2[1]
        
        denom = (x1-x2)*(y3-y4) - (y1-y2)*(x3-x4)
        if abs(denom) < 1e-12:
            return None
            
        px = ((x1*y2 - y1*x2)*(x3-x4) - (x1-x2)*(x3*y4 - y3*x4)) / denom
        py = ((x1*y2 - y1*x2)*(y3-y4) - (y1-y2)*(x3*y4 - y3*x4)) / denom
        
        return (px, py)
    
    def angle_bisector(p1, p2, p3):
        v1 = (p1[0]-p2[0], p1[1]-p2[1])
        v2 = (p3[0]-p2[0], p3[1]-p2[1])
        
        len1 = distance(p1, p2)
        len2 = distance(p3, p2)
        
        if len1 < 1e-12 or len2 < 1e-12:
            return None
            
        v1_norm = (v1[0]/len1, v1[1]/len1)
        v2_norm = (v2[0]/len2, v2[1]/len2)
        
        bisector_dir = (v1_norm[0] + v2_norm[0], v1_norm[1] + v2_norm[1])
        
        bisector_len = math.sqrt(bisector_dir[0]**2 + bisector_dir[1]**2)
        if bisector_len < 1e-12:
            return None
            
        bisector_dir = (bisector_dir[0]/bisector_len, bisector_dir[1]/bisector_len)
        
        return ((p2[0], p2[1]), (p2[0] + bisector_dir[0], p2[1] + bisector_dir[1]))
    
    bisectors = []
    for i in range(n):
        p1 = points[(i-1) % n]
        p2 = points[i]
        p3 = points[(i+1) % n]
        bisector = angle_bisector(p1, p2, p3)
        if bisector:
            bisectors.append(bisector)
    
    if len(bisectors) < 3:
        with open('OUTPUT.TXT', 'w') as f:
            f.write("NO\n")
        return
    
    intersections = []
    for i in range(len(bisectors)):
        for j in range(i+1, len(bisectors)):
            inter = line_intersection(bisectors[i], bisectors[j])
            if inter:
                intersections.append(inter)
    
    if not intersections:
        with open('OUTPUT.TXT', 'w') as f:
            f.write("NO\n")
        return
    
    center_candidate = intersections[0]
    
    def distance_to_line(point, line):
        x0, y0 = point
        x1, y1 = line[0]
        x2, y2 = line[1]
        
        numerator = abs((x2-x1)*(y1-y0) - (x1-x0)*(y2-y1))
        denominator = distance(line[0], line[1])
        
        if denominator < 1e-12:
            return distance(point, line[0])
            
        return numerator / denominator
    
    distances = []
    for i in range(n):
        p1 = points[i]
        p2 = points[(i+1) % n]
        dist = distance_to_line(center_candidate, (p1, p2))
        distances.append(dist)
    
    if all(abs(dist - distances[0]) < 1e-6 for dist in distances):
        radius = distances[0]
        with open('OUTPUT.TXT', 'w') as f:
            f.write("YES\n")
            f.write(f"{center_candidate[0]:.6f} {center_candidate[1]:.6f} {radius:.6f}\n")
    else:
        with open('OUTPUT.TXT', 'w') as f:
            f.write("NO\n")

if __name__ == "__main__":
    main()
