
import math

def main():
    with open("INPUT.TXT", "r") as f:
        data = f.read().split()
    
    X = int(data[0])
    Y = int(data[1])
    R = float(data[2])
    N = int(data[3])
    
    points = []
    index = 4
    for i in range(N):
        xi = int(data[index])
        yi = int(data[index+1])
        index += 2
        points.append((xi, yi))
    
    angles = []
    for xi, yi in points:
        dx = xi - X
        dy = yi - Y
        dist = math.sqrt(dx*dx + dy*dy)
        if dist <= R + 1e-9:
            angle = math.atan2(dy, dx)
            angles.append(angle)
    
    angles.sort()
    n = len(angles)
    for i in range(n):
        angles.append(angles[i] + 2*math.pi)
    
    max_count = 0
    left = 0
    for right in range(n, len(angles)):
        while angles[right] - angles[left] > math.pi + 1e-9:
            left += 1
        max_count = max(max_count, right - left + 1)
    
    print(max_count)

if __name__ == "__main__":
    main()
