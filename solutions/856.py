
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
    
    total = 0
    R = r + q
    R_sq = R * R
    
    if vx == 0:
        for i in range(1, n + 1):
            y_row = i - 1
            if yc > y_row + R or yc + (y_row - R) * vy / abs(vy) > y_row + R:
                continue
            x_center = 0
            for j in range(1, i + 1):
                x_center = -(i - 1) + 2 * (j - 1)
                dx = xc - x_center
                dy = yc - y_row
                if dx * dx + dy * dy <= R_sq:
                    total += 1
    else:
        k = vy / vx
        b = yc - k * xc
        
        for i in range(1, n + 1):
            y_row = i - 1
            if yc > y_row + R:
                continue
                
            x_min = -(i - 1)
            x_max = i - 1
            step = 2
            
            left_j = 1
            right_j = i
            
            while left_j <= right_j:
                j = (left_j + right_j) // 2
                x_center = x_min + (j - 1) * step
                
                dx = xc - x_center
                dy = yc - y_row
                dist_sq = dx * dx + dy * dy
                
                if dist_sq <= R_sq:
                    total += 1
                    break
                
                proj_x = (x_center + k * (y_row - b)) / (1 + k * k) if k != 0 else x_center
                proj_y = k * proj_x + b
                
                if proj_y < y_row:
                    left_j = j + 1
                else:
                    right_j = j - 1
            
            j_mid = (left_j + right_j) // 2
            for offset in [-2, -1, 0, 1, 2]:
                j_test = j_mid + offset
                if 1 <= j_test <= i:
                    x_center = x_min + (j_test - 1) * step
                    dx = xc - x_center
                    dy = yc - y_row
                    if dx * dx + dy * dy <= R_sq:
                        total += 1
                        break
                        
            continue
            
            for j in range(1, i + 1):
                x_center = x_min + (j - 1) * step
                dx = xc - x_center
                dy = yc - y_row
                if dx * dx + dy * dy <= R_sq:
                    total += 1
                    break
    
    print(total)

if __name__ == "__main__":
    main()
