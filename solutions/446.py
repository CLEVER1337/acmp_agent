
n, m = map(int, input().split())
ad = [input().strip() for _ in range(n)]
board = []
for _ in range(n):
    row = list(map(int, input().split()))
    board.append(row)

color_map = {
    'R': 1,
    'G': 2,
    'B': 4,
    '.': 0
}

possible = True
for i in range(n):
    for j in range(m):
        ad_color = ad[i][j]
        board_capability = board[i][j]
        required_color = color_map[ad_color]
        
        if required_color == 0:
            continue
            
        if (board_capability & required_color) == 0:
            possible = False
            break
    
    if not possible:
        break

print('YES' if possible else 'NO')
