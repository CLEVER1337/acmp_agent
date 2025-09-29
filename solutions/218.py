
def main():
    initial_white = ['a1', 'a3', 'b2', 'c1', 'c3', 'd2', 'e1', 'e3', 'f2', 'g1', 'g3', 'h2']
    initial_black = ['a7', 'b6', 'b8', 'c7', 'd6', 'd8', 'e7', 'f6', 'f8', 'g7', 'h6', 'h8']
    
    board = {}
    for row in range(1, 9):
        for col in 'abcdefgh':
            pos = col + str(row)
            if (ord(col) - ord('a') + row) % 2 == 1:
                board[pos] = '-'
            else:
                board[pos] = '.'
                
    for pos in initial_white:
        board[pos] = 'w'
    for pos in initial_black:
        board[pos] = 'b'
        
    n = int(input().strip())
    moves = []
    for _ in range(n):
        moves.append(input().strip())
        
    for i, move in enumerate(moves):
        is_white = i % 2 == 0
        
        if '-' in move:
            parts = move.split('-')
            start, end = parts[0], parts[1]
            piece = board[start]
            board[start] = '-' if board[start] != '.' else '.'
            
            if is_white and end[1] == '8':
                piece = 'W'
            elif not is_white and end[1] == '1':
                piece = 'B'
                
            board[end] = piece
            
        else:
            parts = move.split(':')
            start = parts[0]
            positions = parts
            
            piece = board[start]
            board[start] = '-' if board[start] != '.' else '.'
            
            for j in range(len(positions) - 1):
                from_pos = positions[j]
                to_pos = positions[j + 1]
                
                from_col, from_row = ord(from_pos[0]) - ord('a'), int(from_pos[1])
                to_col, to_row = ord(to_pos[0]) - ord('a'), int(to_pos[1])
                
                col_dir = 1 if to_col > from_col else -1
                row_dir = 1 if to_row > from_row else -1
                
                current_col, current_row = from_col, from_row
                
                while current_col != to_col or current_row != to_row:
                    current_col += col_dir
                    current_row += row_dir
                    pos = chr(ord('a') + current_col) + str(current_row)
                    
                    if board[pos] not in ['.', '-']:
                        board[pos] = '-' if board[pos] != '.' else '.'
                        break
                        
                if is_white and to_pos[1] == '8':
                    piece = 'W'
                elif not is_white and to_pos[1] == '1':
                    piece = 'B'
                    
            board[to_pos] = piece
            
    output = []
    for row in range(8, 0, -1):
        line = []
        for col in 'abcdefgh':
            pos = col + str(row)
            line.append(board[pos])
        output.append(''.join(line))
        
    for line in output:
        print(line)
        
if __name__ == "__main__":
    main()
