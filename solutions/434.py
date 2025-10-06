
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    points = []
    index = 1
    for i in range(n):
        x = int(data[index])
        y = int(data[index + 1])
        index += 2
        points.append((x, y))
    
    min_x = min(points, key=lambda p: p[0])[0]
    max_x = max(points, key=lambda p: p[0])[0]
    min_y = min(points, key=lambda p: p[1])[1]
    max_y = max(points, key=lambda p: p[1])[1]
    
    result_points = [
        (min_x - 1, min_y - 1),
        (max_x + 1, min_y - 1),
        (max_x + 1, max_y + 1),
        (min_x - 1, max_y + 1)
    ]
    
    print(4)
    for point in result_points:
        print(f"{point[0]} {point[1]}")

if __name__ == "__main__":
    main()
