
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    points = []
    for i in range(n):
        x = int(data[2*i+1])
        y = int(data[2*i+2])
        points.append((x, y))
    
    if n < 2:
        print(0)
        return
        
    total = 0
    for i in range(n):
        for j in range(i+1, n):
            a = points[i]
            b = points[j]
            dx = b[0] - a[0]
            dy = b[1] - a[1]
            
            left_count = 0
            right_count = 0
            
            for k in range(n):
                if k == i or k == j:
                    continue
                    
                p = points[k]
                cross = (p[0] - a[0]) * dy - (p[1] - a[1]) * dx
                
                if cross > 0:
                    left_count += 1
                elif cross < 0:
                    right_count += 1
            
            if left_count > 0 and right_count > 0:
                total += 1
    
    print(total)

if __name__ == "__main__":
    main()
