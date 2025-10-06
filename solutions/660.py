
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        print(0)
        return
        
    n = int(data[0])
    m = int(data[1])
    k = int(data[2])
    
    bad_cells = []
    index = 3
    for i in range(k):
        r = int(data[index])
        c = int(data[index+1])
        index += 2
        bad_cells.append((r, c))
    
    total_rectangles = n * (n + 1) // 2 * m * (m + 1) // 2
    
    if k == 0:
        print(total_rectangles)
        return
        
    bad_cells.sort(key=lambda x: (x[0], x[1]))
    
    left = [[0] * (m + 2) for _ in range(n + 2)]
    right = [[0] * (m + 2) for _ in range(n + 2)]
    up = [[0] * (m + 2) for _ in range(n + 2)]
    down = [[0] * (m + 2) for _ in range(n + 2)]
    
    for i in range(n + 2):
        for j in range(m + 2):
            left[i][j] = j - 1
            right[i][j] = j + 1
            up[i][j] = i - 1
            down[i][j] = i + 1
    
    for r, c in bad_cells:
        up[down[r][c]][c] = up[r][c]
        down[up[r][c]][c] = down[r][c]
        left[r][right[r][c]] = left[r][c]
        right[r][left[r][c]] = right[r][c]
    
    result = 0
    for r, c in bad_cells:
        u = r - up[r][c]
        d = down[r][c] - r
        l = c - left[r][c]
        ri = right[r][c] - c
        
        result += u * d * l * ri
    
    print(total_rectangles - result)
    
if __name__ == "__main__":
    main()
