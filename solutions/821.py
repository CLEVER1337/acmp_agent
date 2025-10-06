
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
    
    empty_i, empty_j = n-1, n-1
    
    for idx, cmd in enumerate(commands, 1):
        new_i, new_j = empty_i, empty_j
        
        if cmd == 'U':
            new_i -= 1
        elif cmd == 'D':
            new_i += 1
        elif cmd == 'L':
            new_j -= 1
        elif cmd == 'R':
            new_j += 1
        
        if new_i < 0 or new_i >= n or new_j < 0 or new_j >= n:
            print(f"ERROR {idx}")
            return
        
        board[empty_i][empty_j], board[new_i][new_j] = board[new_i][new_j], board[empty_i][empty_j]
        empty_i, empty_j = new_i, new_j
    
    for i in range(n):
        print(' '.join(str(x) for x in board[i]))

if __name__ == "__main__":
    main()
