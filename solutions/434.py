
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    points = []
    index = 1
    for i in range(n):
        x = int(data[index])
        y = int(data[index+1])
        index += 2
        points.append((x, y))
    
    min_x = min(p[0] for p in points)
    max_x = max(p[0] for p in points)
    min_y = min(p[1] for p in points)
    max_y = max(p[1] for p in points)
    
    fence = [
        (min_x - 1, min_y - 1),
        (max_x + 1, min_y - 1),
        (max_x + 1, max_y + 1),
        (min_x - 1, max_y + 1)
    ]
    
    print(4)
    for p in fence:
        print(f"{p[0]} {p[1]}")

if __name__ == "__main__":
    main()
