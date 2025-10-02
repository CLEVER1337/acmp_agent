
def main():
    board = []
    with open('INPUT.TXT', 'r') as f:
        for i in range(8):
            line = f.readline().strip()
            board.append(list(line))
    
    white_captures = set()
    black_captures = set()
    
    directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    
    def dfs_captures(x, y, color, captures, path=None):
        if path is None:
            path = set()
        current_captures = set()
        max_depth_captures = set()
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            jx, jy = x + 2*dx, y + 2*dy
            
            if (0 <= jx < 8 and 0 <= jy < 8 and 
                0 <= nx < 8 and 0 <= ny < 8):
                
                opponent = 'B' if color == 'W' else 'W'
                if (board[nx][ny] == opponent and 
                    board[jx][jy] == '.' and 
                    (jx, jy) not in path):
                    
                    capture_pos = (nx, ny)
                    current_captures.add(capture_pos)
                    
                    original = board[x][y]
                    captured = board[nx][ny]
                    
                    board[x][y] = '.'
                    board[nx][ny] = '.'
                    board[jx][jy] = color
                    
                    path.add((jx, jy))
                    deeper_captures = dfs_captures(jx, jy, color, captures, path)
                    path.remove((jx, jy))
                    
                    board[x][y] = original
                    board[nx][ny] = captured
                    board[jx][jy] = '.'
                    
                    if deeper_captures:
                        max_depth_captures.update(deeper_captures)
        
        if max_depth_captures:
            return max_depth_captures
        return current_captures
    
    for i in range(8):
        for j in range(8):
            if board[i][j] == 'W':
                captures = dfs_captures(i, j, 'W', white_captures)
                white_captures.update(captures)
            elif board[i][j] == 'B':
                captures = dfs_captures(i, j, 'B', black_captures)
                black_captures.update(captures)
    
    white_list = sorted(white_captures, key=lambda x: (x[0], x[1]))
    black_list = sorted(black_captures, key=lambda x: (x[0], x[1]))
    
    with open('OUTPUT.TXT', 'w') as f:
        if white_list:
            f.write("White takes:")
            for i, (x, y) in enumerate(white_list):
                if i % 8 == 0:
                    f.write("\n")
                f.write(f"({x+1},{y+1}) ")
            f.write("\n")
        else:
            f.write("White takes: None\n")
            
        if black_list:
            f.write("Black takes:")
            for i, (x, y) in enumerate(black_list):
                if i % 8 == 0:
                    f.write("\n")
                f.write(f"({x+1},{y+1}) ")
            f.write("\n")
        else:
            f.write("Black takes: None\n")

if __name__ == "__main__":
    main()
