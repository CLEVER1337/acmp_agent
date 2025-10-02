
import math

def main():
    import sys
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    engines = []
    for i in range(1, n + 1):
        parts = data[i].split()
        if len(parts) < 2:
            continue
        magnitude = float(parts[0])
        angle_deg = float(parts[1])
        angle_rad = math.radians(angle_deg)
        x = magnitude * math.cos(angle_rad)
        y = magnitude * math.sin(angle_rad)
        engines.append((x, y, i))
    
    total_x = 0.0
    total_y = 0.0
    selected = []
    
    for x, y, idx in engines:
        dot_product = total_x * x + total_y * y
        if dot_product > 0:
            total_x += x
            total_y += y
            selected.append(idx)
    
    print(len(selected))
    if selected:
        print(" ".join(map(str, selected)))
    else:
        print()

if __name__ == "__main__":
    main()
