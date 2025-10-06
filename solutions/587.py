
import math

def main():
    import sys
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    engines = []
    for i in range(1, n + 1):
        parts = data[i].split()
        mag = float(parts[0])
        angle_deg = float(parts[1])
        angle_rad = math.radians(angle_deg)
        x = mag * math.cos(angle_rad)
        y = mag * math.sin(angle_rad)
        engines.append((x, y, i))
    
    engines.sort(key=lambda v: math.atan2(v[1], v[0]))
    
    total_x = sum(x for x, y, idx in engines)
    total_y = sum(y for x, y, idx in engines)
    
    best_sq = total_x**2 + total_y**2
    best_start = 0
    best_end = n - 1
    
    j = 0
    current_x = 0.0
    current_y = 0.0
    
    for i in range(n):
        while True:
            next_j = (j + 1) % n
            if next_j == i:
                break
            dx1 = current_x + engines[j][0]
            dy1 = current_y + engines[j][1]
            dx2 = current_x + engines[next_j][0]
            dy2 = current_y + engines[next_j][1]
            if dx1**2 + dy1**2 >= dx2**2 + dy2**2:
                break
            current_x += engines[j][0]
            current_y += engines[j][1]
            j = next_j
        
        current_sq = current_x**2 + current_y**2
        if current_sq > best_sq:
            best_sq = current_sq
            best_start = i
            best_end = j
        
        current_x -= engines[i][0]
        current_y -= engines[i][1]
        
        if j == i:
            j = (j + 1) % n
            current_x = 0.0
            current_y = 0.0
    
    indices = []
    i = best_start
    while True:
        indices.append(engines[i][2])
        if i == best_end:
            break
        i = (i + 1) % n
    
    print(len(indices))
    print(" ".join(map(str, indices)))

if __name__ == "__main__":
    main()
