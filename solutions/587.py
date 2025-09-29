
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
        engines.append((mag, angle_rad, i))
    
    engines_sorted = sorted(engines, key=lambda x: x[1])
    
    total_x = 0.0
    total_y = 0.0
    selected_indices = []
    
    for i in range(n):
        mag, angle, idx = engines_sorted[i]
        test_x = total_x + mag * math.cos(angle)
        test_y = total_y + mag * math.sin(angle)
        new_mag = math.sqrt(test_x**2 + test_y**2)
        current_mag = math.sqrt(total_x**2 + total_y**2)
        
        if new_mag >= current_mag:
            total_x = test_x
            total_y = test_y
            selected_indices.append(idx)
    
    selected_indices.sort()
    print(len(selected_indices))
    print(" ".join(map(str, selected_indices)))

if __name__ == "__main__":
    main()
