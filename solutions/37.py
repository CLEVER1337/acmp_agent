
import math

def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    q = float(data[1])
    points = []
    index = 2
    for i in range(n):
        x1 = int(data[index])
        y1 = int(data[index+1])
        x2 = int(data[index+2])
        y2 = int(data[index+3])
        index += 4
        points.append((x1, y1, x2, y2))
    
    for point in points:
        x1, y1, x2, y2 = point
        norm_x = math.sqrt(x1**2 + y1**2)
        norm_ax = math.sqrt(x2**2 + y2**2)
        
        if norm_x == 0:
            if norm_ax > 0:
                print("No")
                return
            else:
                continue
                
        if norm_ax > q * norm_x:
            print("No")
            return
            
    print("Yes")

if __name__ == "__main__":
    main()
