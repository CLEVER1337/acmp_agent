
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    squares = []
    index = 1
    for i in range(n):
        x = int(data[index])
        y = int(data[index+1])
        l = int(data[index+2])
        index += 3
        squares.append((x, y, l))
    
    diff_shapes = {}
    
    for i in range(n):
        x1, y1, l1 = squares[i]
        for j in range(n):
            if i == j:
                continue
            x2, y2, l2 = squares[j]
            if x1 <= x2 and y1 <= y2 and x1 + l1 >= x2 + l2 and y1 + l1 >= y2 + l2:
                dx1 = x2 - x1
                dx2 = (x1 + l1) - (x2 + l2)
                dy1 = y2 - y1
                dy2 = (y1 + l1) - (y2 + l2)
                key = (dx1, dx2, dy1, dy2)
                if key not in diff_shapes:
                    diff_shapes[key] = []
                diff_shapes[key].append((i, j))
    
    count = 0
    for key, pairs in diff_shapes.items():
        k = len(pairs)
        if k >= 2:
            count += k * (k - 1)
    
    print(count)

if __name__ == "__main__":
    main()
