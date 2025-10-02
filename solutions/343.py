
n, m = map(int, input().split())
k = int(input())

floor = [[False] * m for _ in range(n)]
covered_area = 0

for _ in range(k):
    tile_type, y, x = map(int, input().split())
    
    if tile_type == 1:
        cells = [(y, x+1), (y+1, x), (y+1, x+1)]
    elif tile_type == 2:
        cells = [(y, x), (y+1, x), (y+1, x+1)]
    elif tile_type == 3:
        cells = [(y, x), (y, x+1), (y+1, x)]
    elif tile_type == 4:
        cells = [(y, x), (y, x+1), (y+1, x+1)]
    
    valid = True
    for cy, cx in cells:
        if cy < 0 or cy >= n or cx < 0 or cx >= m or floor[cy][cx]:
            valid = False
            break
    
    if valid:
        for cy, cx in cells:
            floor[cy][cx] = True
            covered_area += 1

print(covered_area)
