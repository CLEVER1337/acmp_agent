
def main():
    import sys
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    commands = data[1].strip()
    
    board = []
    num = 1
    for i in range(n):
        row = []
        for j in range(n):
            if i == n-1 and j == n-1:
                row.append(0)
            else:
                row.append(num)
                num += 1
        board.append(row)
    
    empty_row = n - 1
    empty_col = n - 1
    
    for idx, cmd in enumerate(commands):
        if cmd == 'U':
            if empty_row == 0:
                print(f"ERROR {idx + 1}")
                return
            board[empty_row][empty_col], board[empty_row-1][empty_col] = board[empty_row-1][empty_col], board[empty_row][empty_col]
            empty_row -= 1
        elif cmd == 'D':
            if empty_row == n - 1:
                print(f"ERROR {idx + 1}")
                return
            board[empty_row][empty_col], board[empty_row+1][empty_col] = board[empty_row+1][empty_col], board[empty_row][empty_col]
            empty_row += 1
        elif cmd == 'L':
            if empty_col == 0:
                print(f"ERROR {idx + 1}")
                return
            board[empty_row][empty_col], board[empty_row][empty_col-1] = board[empty_row][empty_col-1], board[empty_row][empty_col]
            empty_col -= 1
        elif cmd == 'R':
            if empty_col == n - 1:
                print(f"ERROR {idx + 1}")
                return
            board[empty_row][empty_col], board[empty_row][empty_col+1] = board[empty_row][empty_col+1], board[empty_row][empty_col]
            empty_col += 1
    
    for i in range(n):
        line = []
        for j in range(n):
            line.append(str(board[i][j]))
        print(' '.join(line))

if __name__ == "__main__":
    main()
