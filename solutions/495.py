
import math

def main():
    with open('INPUT.TXT', 'r') as f:
        n = int(f.readline().strip())
        points = []
        for _ in range(n):
            x, y = map(int, f.readline().split())
            points.append((x, y))
        k = int(f.readline().strip())
    
    for _ in range(k):
        new_points = []
        for i in range(len(points)):
            x1, y1 = points[i]
            x2, y2 = points[(i + 1) % len(points)]
            mid_x = (x1 + x2) / 2.0
            mid_y = (y1 + y2) / 2.0
            new_points.append((mid_x, mid_y))
        points = new_points
    
    total_length = 0.0
    for i in range(len(points)):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % len(points)]
        dx = x2 - x1
        dy = y2 - y1
        total_length += math.sqrt(dx*dx + dy*dy)
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write("{:.15f}".format(total_length))

if __name__ == "__main__":
    main()
