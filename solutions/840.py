
import math

def read_floats():
    return list(map(float, input().split()))

def distance(x1, y1, z1, x2, y2, z2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2)

def main():
    data = read_floats()
    X, Y, Z, R = data
    n = int(input().strip())
    
    spheres = []
    for i in range(n):
        data = read_floats()
        spheres.append((data[0], data[1], data[2], data[3], i + 1))
    
    added = [False] * (n + 1)
    added[0] = True
    
    queue = [0]
    stop_ball = 0
    
    while queue:
        current_idx = queue.pop(0)
        if current_idx == 0:
            cx, cy, cz, cr = X, Y, Z, R
        else:
            ball = spheres[current_idx - 1]
            cx, cy, cz, cr, _ = ball
        
        for i in range(1, n + 1):
            if not added[i]:
                ball = spheres[i - 1]
                nx, ny, nz, nr, num = ball
                dist = distance(cx, cy, cz, nx, ny, nz)
                if dist <= cr + nr:
                    added[i] = True
                    queue.append(i)
                    if stop_ball == 0 or num > stop_ball:
                        stop_ball = num
    
    for i in range(1, n + 1):
        if not added[i]:
            stop_ball = 0
            break
    
    print(stop_ball)

if __name__ == "__main__":
    main()
