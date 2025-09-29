
from collections import deque

def flip_bit(bit):
    return '1' if bit == '0' else '0'

def flip_board(board, pos):
    row, col = pos // 4, pos % 4
    new_board = list(board)
    
    positions_to_flip = []
    positions_to_flip.append(pos)
    
    if row > 0:
        positions_to_flip.append(pos - 4)
    if row < 3:
        positions_to_flip.append(pos + 4)
    if col > 0:
        positions_to_flip.append(pos - 1)
    if col < 3:
        positions_to_flip.append(pos + 1)
    
    for p in positions_to_flip:
        new_board[p] = flip_bit(new_board[p])
    
    return ''.join(new_board)

def solve(input_board):
    board_str = ''.join(['1' if c == 'b' else '0' for row in input_board for c in row])
    target1 = '0' * 16
    target2 = '1' * 16
    
    if board_str == target1 or board_str == target2:
        return 0
    
    queue = deque([(board_str, 0)])
    visited = {board_str}
    
    while queue:
        current_board, moves = queue.popleft()
        
        if current_board == target1 or current_board == target2:
            return moves
        
        for pos in range(16):
            new_board = flip_board(current_board, pos)
            if new_board not in visited:
                visited.add(new_board)
                queue.append((new_board, moves + 1))
    
    return "Impossible"

def main():
    with open('INPUT.TXT', 'r') as f:
        input_board = [line.strip() for line in f.readlines()]
    
    result = solve(input_board)
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(result))

if __name__ == "__main__":
    main()
