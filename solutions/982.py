
def main():
    board = []
    with open('INPUT.TXT', 'r') as f:
        for i in range(8):
            line = f.readline().strip()
            board.append(list(line))
    
    white_captures = set()
    black_captures = set()
    
    directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    
    def dfs(i, j, color, captured, visited):
        nonlocal max_captures
        found = False
        for dx, dy in directions:
            ni1, nj1 = i + dx, j + dy
            ni2, nj2 = i + 2*dx, j + 2*dy
            
            if 0 <= ni1 < 8 and 0 <= nj1 < 8 and 0 <= ni2 < 8 and 0 <= nj2 < 8:
                if color == 'W':
                    opponent = 'B'
                else:
                    opponent = 'W'
                
                if (board[ni1][nj1] == opponent and 
                    board[ni2][nj2] == '.' and 
                    (ni1, nj1) not in captured):
                    
                    new_captured = captured | {(ni1, nj1)}
                    if (ni2, nj2) not in visited:
                        visited.add((ni2, nj2))
                        found = True
                        dfs(ni2, nj2, color, new_captured, visited.copy())
        
        if not found and captured:
            for cap in captured:
                if color == 'W':
                    white_captures.add(cap)
                else:
                    black_captures.add(cap)
    
    for i in range(8):
        for j in range(8):
            if board[i][j] == 'W':
                visited = set()
                visited.add((i, j))
                dfs(i, j, 'W', set(), visited)
            elif board[i][j] == 'B':
                visited = set()
                visited.add((i, j))
                dfs(i, j, 'B', set(), visited)
    
    white_list = sorted(white_captures)
    black_list = sorted(black_captures)
    
    with open('OUTPUT.TXT', 'w') as f:
        if white_list:
            f.write("White captures:")
            for i, j in white_list:
                f.write(f" ({i+1},{j+1})")
            f.write("\n")
        else:
            f.write("White captures:\n")
            
        if black_list:
            f.write("Black captures:")
            for i, j in black_list:
                f.write(f" ({i+1},{j+1})")
            f.write("\n")
        else:
            f.write("Black captures:\n")

if __name__ == "__main__":
    main()
