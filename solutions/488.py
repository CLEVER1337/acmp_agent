
import sys
import math

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    R = float(data[0])
    K = int(data[1])
    
    lines = []
    for i in range(K):
        idx = 2 + i * 4
        x1, y1, x2, y2 = map(float, data[idx:idx+4])
        lines.append((x1, y1, x2, y2))
    
    chords = []
    for x1, y1, x2, y2 in lines:
        if x1 == x2 and y1 == y2:
            continue
            
        A = y2 - y1
        B = x1 - x2
        C = x2 * y1 - x1 * y2
        
        dist = abs(C) / math.sqrt(A*A + B*B)
        if dist < R:
            chord_length = 2 * math.sqrt(R*R - dist*dist)
            chords.append((A, B, C, dist, chord_length))
    
    n = len(chords)
    intersections = 0
    
    for i in range(n):
        A1, B1, C1, dist1, len1 = chords[i]
        for j in range(i + 1, n):
            A2, B2, C2, dist2, len2 = chords[j]
            
            det = A1 * B2 - A2 * B1
            if abs(det) < 1e-12:
                continue
                
            x = (B1 * C2 - B2 * C1) / det
            y = (A2 * C1 - A1 * C2) / det
            
            if x*x + y*y < R*R - 1e-12:
                intersections += 1
    
    parts = 1 + n + intersections
    print(parts)

if __name__ == "__main__":
    main()
