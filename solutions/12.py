
import sys

def point_in_rectangle(px, py, rect):
    x1, y1, x2, y2, x3, y3, x4, y4 = rect
    points = [(x1, y1), (x2, y2), (x3, y3), (x4, y4)]
    
    min_x = min(p[0] for p in points)
    max_x = max(p[0] for p in points)
    min_y = min(p[1] for p in points)
    max_y = max(p[1] for p in points)
    
    return min_x <= px <= max_x and min_y <= py <= max_y

def main():
    data = sys.stdin.read().split()
    if not data:
        print(0)
        return
        
    n = int(data[0])
    index = 1
    count = 0
    
    for _ in range(n):
        x = int(data[index]); y = int(data[index+1]); index += 2
        rect = list(map(int, data[index:index+8]))
        index += 8
        
        if point_in_rectangle(x, y, rect):
            count += 1
            
    print(count)

if __name__ == "__main__":
    main()
