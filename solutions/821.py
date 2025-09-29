
def main():
    import sys
    data = sys.stdin.read().splitlines()
    if not data:
        return
    
    n = int(data[0])
    moves = data[1].strip()
    
    board = []
    num = 1
    for i in range(n):
        row = []
        for j in range(n):
            if i == n - 1 and j == n - 1:
                row.append(0)
            else:
                row.append(num)
                num += 1
        board.append(row)
    
    empty_i, empty_j = n - 1, n - 1
    
    for idx, move in enumerate(moves, 1):
        di, dj = 0, 0
        if move == 'U':
            di = -1
        elif move == 'D':
            di = 1
        elif move == 'L':
            dj = -1
        elif move == 'R':
            dj = 1
        
        new_i, new_j = empty_i + di, empty_j + dj
        
        if new_i < 0 or new_i >= n or new_j < 0 or new_j >= n:
            print(f"ERROR {idx}")
            return
        
        board[empty_i][empty_j], board[new_i][new_j] = board[new_i][new_j], board[empty_i][empty_j]
        empty_i, empty_j = new_i, new_j
    
    for i in range(n):
        line = []
        for j in range(n):
            line.append(str(board[i][j]))
        print(' '.join(line))

if __name__ == "__main__":
    main()
