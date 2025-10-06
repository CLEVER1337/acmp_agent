
import math

def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    bx = int(data[1])
    by = int(data[2])
    L = int(data[3])
    
    points = []
    index = 4
    for i in range(n):
        x = int(data[index])
        y = int(data[index+1])
        index += 2
        points.append((x, y))
    
    for i in range(n):
        x, y = points[i]
        dx = x - bx
        dy = y - by
        distance_sq = dx*dx + dy*dy
        if distance_sq <= L*L:
            print(i+1)
            return
            
    print("Yes")

if __name__ == "__main__":
    main()
