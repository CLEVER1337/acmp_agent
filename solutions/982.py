
def main():
    board = []
    for _ in range(8):
        line = input().strip()
        board.append(list(line))
    
    white_captures = set()
    black_captures = set()
    
    directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    
    def find_captures(color, opponent_color, start_i, start_j, visited=None):
        if visited is None:
            visited = set()
        captures = set()
        key = (start_i, start_j)
        if key in visited:
            return captures
        visited.add(key)
        
        for di, dj in directions:
            ni1, nj1 = start_i + di, start_j + dj
            ni2, nj2 = start_i + 2*di, start_j + 2*dj
            
            if 0 <= ni1 < 8 and 0 <= nj1 < 8 and 0 <= ni2 < 8 and 0 <= nj2 < 8:
                if (board[ni1][nj1] == opponent_color and 
                    board[ni2][nj2] == '.'):
                    captures.add((ni1, nj1))
                    new_visited = visited.copy()
                    board_copy = [row[:] for row in board]
                    board_copy[ni1][nj1] = '.'
                    board_copy[start_i][start_j] = '.'
                    board_copy[ni2][nj2] = color
                    further_captures = find_captures(color, opponent_color, ni2, nj2, new_visited)
                    captures.update(further_captures)
        
        return captures
    
    for i in range(8):
        for j in range(8):
            if board[i][j] == 'W':
                caps = find_captures('W', 'B', i, j)
                white_captures.update(caps)
            elif board[i][j] == 'B':
                caps = find_captures('B', 'W', i, j)
                black_captures.update(caps)
    
    white_list = sorted(white_captures, key=lambda x: (x[0], x[1]))
    black_list = sorted(black_captures, key=lambda x: (x[0], x[1]))
    
    if not white_list and not black_list:
        print("No captures")
    else:
        if white_list:
            print("White captures:")
            for i, j in white_list:
                print(f"({i+1}, {j+1})")
        if black_list:
            print("Black captures:")
            for i, j in black_list:
                print(f"({i+1}, {j+1})")

if __name__ == "__main__":
    main()
