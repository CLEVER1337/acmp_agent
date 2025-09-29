
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    points = []
    index = 1
    for i in range(n):
        x = int(data[index])
        y = int(data[index + 1])
        index += 2
        points.append((x, y))
    
    def is_point_inside(x, y):
        winding_number = 0
        for i in range(n):
            x1, y1 = points[i]
            x2, y2 = points[(i + 1) % n]
            
            if y1 <= y:
                if y2 > y and (x2 - x1) * (y - y1) - (x - x1) * (y2 - y1) > 0:
                    winding_number += 1
            else:
                if y2 <= y and (x2 - x1) * (y - y1) - (x - x1) * (y2 - y1) < 0:
                    winding_number -= 1
        
        return winding_number != 0
    
    min_x = min(p[0] for p in points)
    max_x = max(p[0] for p in points)
    min_y = min(p[1] for p in points)
    max_y = max(p[1] for p in points)
    
    count = 0
    for x in range(min_x + 1, max_x):
        for y in range(min_y + 1, max_y):
            if is_point_inside(x, y):
                count += 1
    
    print(count)

if __name__ == "__main__":
    main()
