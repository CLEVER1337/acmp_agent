
import math

def main():
    with open("INPUT.TXT", "r") as f:
        n = int(f.readline())
        points = []
        for _ in range(n):
            x, y = map(int, f.readline().split())
            points.append((x, y))
    
    distances = set()
    for i in range(n):
        for j in range(i + 1, n):
            dx = points[i][0] - points[j][0]
            dy = points[i][1] - points[j][1]
            distance = math.sqrt(dx*dx + dy*dy)
            distances.add(distance)
    
    sorted_distances = sorted(distances)
    
    with open("OUTPUT.TXT", "w") as f:
        f.write(f"{len(sorted_distances)}\n")
        for d in sorted_distances:
            f.write(f"{d:.15f}\n")

if __name__ == "__main__":
    main()
