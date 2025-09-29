
import math

def main():
    with open("INPUT.TXT", "r") as f:
        x1, y1 = map(int, f.readline().split())
        x2, y2 = map(int, f.readline().split())
        r = int(f.readline())
        s = int(f.readline())
    
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    if distance >= 2 * r:
        total_area = 2 * math.pi * r * r
    else:
        d = distance
        alpha = 2 * math.acos(d / (2 * r))
        segment_area = (r * r / 2) * (alpha - math.sin(alpha))
        total_area = 2 * math.pi * r * r - 2 * segment_area
    
    if total_area > s + 1e-6:
        result = "YES"
    else:
        result = "NO"
    
    with open("OUTPUT.TXT", "w") as f:
        f.write(result)

if __name__ == "__main__":
    main()
