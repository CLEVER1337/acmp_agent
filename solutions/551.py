
import math

def main():
    data = input().split()
    R = int(data[0])
    r = int(data[1])
    h = int(data[2])
    b = int(data[3])
    
    d = b
    if d < r:
        d = r
        
    if d == 0:
        if h <= R - r:
            print("YES")
        else:
            print("NO")
    else:
        sin_alpha = r / d
        cos_alpha = math.sqrt(1 - sin_alpha * sin_alpha)
        max_h = (R - d * cos_alpha) / sin_alpha
        
        if h <= max_h:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()
