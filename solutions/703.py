
from collections import deque

def parse_input():
    with open('INPUT.TXT', 'r') as f:
        lines = f.readlines()
    
    start_board = []
    end_board = []
    
    for line in lines:
        parts = line.strip().split()
        start_row = parts[0]
        end_row = parts[1]
        start_board.append(start_row)
        end_board.append(end_row)
    
    return start_board, end_board

def board_to_state(board):
    white_pos = []
    black_pos = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'W':
                white_pos.append((i, j))
            elif board[i][j] == 'B':
                black_pos.append((i, j))
    return tuple(sorted(white_pos) + sorted(black_pos))

def is_valid_move(x, y):
    return 0 <= x < 3 and 0 <= y < 3

def get_knight_moves(x, y):
    moves = []
    for dx, dy in [(2,1), (2,-1), (-2,1), (-2,-1), (1,2), (1,-2), (-1,2), (-1,-2)]:
        nx, ny = x + dx, y + dy
        if is_valid_move(nx, ny):
            moves.append((nx, ny))
    return moves

def solve():
    start_board, end_board = parse_input()
    start_state = board_to_state(start_board)
    end_state = board_to_state(end_board)
    
    visited = {}
    queue = deque([(start_state, 0)])
    visited[start_state] = True
    
    while queue:
        state, moves = queue.popleft()
        
        if state == end_state:
            return moves
        
        pieces = list(state)
        
        for piece_idx in range(4):
            x, y = pieces[piece_idx]
            
            for nx, ny in get_knight_moves(x, y):
                if (nx, ny) in pieces:
                    continue
                
                new_pieces = pieces.copy()
                new_pieces[piece_idx] = (nx, ny)
                
                new_state = tuple(sorted(new_pieces[:2]) + sorted(new_pieces[2:]))
                
                if new_state not in visited:
                    visited[new_state] = True
                    queue.append((new_state, moves + 1))
    
    return -1

result = solve()
with open('OUTPUT.TXT', 'w') as f:
    f.write(str(result))
