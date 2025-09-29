
import math

def main():
    import sys
    data = sys.stdin.read().split()
    r = int(data[0])
    n = int(data[1])
    q = int(data[2])
    xc = int(data[3])
    yc = int(data[4])
    vx = int(data[5])
    vy = int(data[6])
    
    total_hit = 0
    R = r + q
    
    for i in range(1, n + 1):
        row_y = i - 1
        for j in range(i):
            x_keg = -(i - 1) + 2 * j
            y_keg = row_y
            
            A = vx * vx + vy * vy
            B = 2 * (vx * (xc - x_keg) + vy * (yc - y_keg))
            C = (xc - x_keg) ** 2 + (yc - y_keg) ** 2 - R * R
            
            discriminant = B * B - 4 * A * C
            
            if discriminant < 0:
                continue
                
            t1 = (-B - math.sqrt(discriminant)) / (2 * A)
            t2 = (-B + math.sqrt(discriminant)) / (2 * A)
            
            if t2 >= 0:
                total_hit += 1
                
    print(total_hit)

if __name__ == "__main__":
    main()
