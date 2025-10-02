
import math

def readints():
    return list(map(int, input().split()))

def main():
    r, n = readints()
    q = int(input())
    xc, yc = readints()
    vx, vy = readints()
    
    total = 0
    for i in range(1, n + 1):
        y_row = i - 1
        for j in range(1, i + 1):
            x_center = -(i - 1) + 2 * (j - 1)
            
            A = vx**2 + vy**2
            B = 2 * (vx * (xc - x_center) + vy * (yc - y_row))
            C = (xc - x_center)**2 + (yc - y_row)**2 - (r + q)**2
            
            discriminant = B**2 - 4 * A * C
            
            if discriminant >= 0:
                t1 = (-B - math.sqrt(discriminant)) / (2 * A)
                t2 = (-B + math.sqrt(discriminant)) / (2 * A)
                
                if (t1 >= 0 and t1 <= 1) or (t2 >= 0 and t2 <= 1) or (t1 <= 0 and t2 >= 0):
                    total += 1
                    
    print(total)

if __name__ == "__main__":
    main()
