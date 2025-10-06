
import sys

def main():
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    points = []
    for i in range(1, n + 1):
        x, y = map(int, data[i].split())
        points.append((x, y))
    
    point_set = set(points)
    count = 0
    
    for i in range(n):
        x1, y1 = points[i]
        for j in range(i + 1, n):
            x2, y2 = points[j]
            if x1 == x2 or y1 == y2:
                continue
            if (x1, y2) in point_set and (x2, y1) in point_set:
                count += 1
    
    print(count // 2)

if __name__ == "__main__":
    main()
