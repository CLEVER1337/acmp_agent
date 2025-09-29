
import math

def main():
    with open('INPUT.TXT', 'r') as f:
        data = f.read().split()
    
    n = int(data[0])
    alpha = int(data[1])
    x0 = int(data[2])
    y0 = int(data[3])
    
    angles = []
    for i in range(4, 4 + 2 * n, 2):
        x = int(data[i])
        y = int(data[i + 1])
        dx = x - x0
        dy = y - y0
        angle = math.atan2(dy, dx)
        angles.append(math.degrees(angle))
    
    for i in range(len(angles)):
        if angles[i] < 0:
            angles[i] += 360
    
    angles.sort()
    double_angles = angles + [a + 360 for a in angles]
    
    if alpha == 360:
        print(1)
        return
    
    shots = float('inf')
    left = 0
    for right in range(len(double_angles)):
        while double_angles[right] - double_angles[left] > alpha + 1e-9:
            left += 1
        if right - left + 1 >= n:
            shots = min(shots, 1)
    
    if shots == 1:
        print(1)
        return
    
    for i in range(len(angles)):
        covered = 1
        current_angle = angles[i]
        count = 1
        
        for j in range(1, len(angles)):
            idx = (i + j) % len(angles)
            diff = angles[idx] - current_angle
            if diff < 0:
                diff += 360
            
            if diff > alpha + 1e-9:
                covered += 1
                current_angle = angles[idx]
                count += 1
        
        shots = min(shots, count)
    
    print(shots)

if __name__ == "__main__":
    main()
