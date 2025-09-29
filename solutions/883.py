
import sys
import math

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    circles = []
    index = 1
    for i in range(n):
        r = int(data[index])
        c = int(data[index + 1])
        index += 2
        circles.append((r, c, i))
    
    centers = []
    for i in range(n):
        if i == 0:
            centers.append((0.0, 0.0))
        else:
            r_prev, c_prev, idx_prev = circles[i-1]
            r_curr, c_curr, idx_curr = circles[i]
            min_dist = r_prev + r_curr + 0.01
            x_prev, y_prev = centers[i-1]
            angle = math.pi * (i - 1) / 10.0
            x_curr = x_prev + min_dist * math.cos(angle)
            y_curr = y_prev + min_dist * math.sin(angle)
            centers.append((x_curr, y_curr))
    
    for center in centers:
        print(f"{center[0]:.6f} {center[1]:.6f}")

if __name__ == "__main__":
    main()
