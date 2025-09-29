
n, m = map(int, input().split())
grid = [input().strip() for _ in range(n)]

min_gap = float('inf')

for i in range(n):
    a_end = -1
    b_start = m
    
    for j in range(m):
        if grid[i][j] == 'A':
            a_end = max(a_end, j)
        elif grid[i][j] == 'B':
            b_start = min(b_start, j)
    
    if a_end != -1 and b_start != m:
        gap = b_start - a_end - 1
        if gap < min_gap:
            min_gap = gap

if min_gap == float('inf'):
    print(0)
else:
    print(max(0, min_gap))
