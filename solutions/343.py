
n, m = map(int, input().split())
k = int(input())

grid = [[False] * m for _ in range(n)]

for _ in range(k):
    t, y, x = map(int, input().split())
    
    if t == 1:
        squares = [(y, x), (y, x+1), (y+1, x)]
    elif t == 2:
        squares = [(y, x), (y, x+1), (y+1, x+1)]
    elif t == 3:
        squares = [(y, x), (y+1, x), (y+1, x+1)]
    elif t == 4:
        squares = [(y, x+1), (y+1, x), (y+1, x+1)]
    
    valid = True
    for i, j in squares:
        if i < 0 or i >= n or j < 0 or j >= m or grid[i][j]:
            valid = False
            break
    
    if valid:
        for i, j in squares:
            grid[i][j] = True

count = sum(sum(row) for row in grid)
print(count)
