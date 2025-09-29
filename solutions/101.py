
def main():
    with open("INPUT.TXT", "r") as f:
        data = f.read().split()
        N = int(data[0])
        K = int(data[1])
    
    if K == 0:
        with open("OUTPUT.TXT", "w") as f:
            f.write("1")
        return
    
    board = [[0] * N for _ in range(N)]
    count = 0
    
    def can_place(row, col):
        for i in range(N):
            if board[row][i] == 1 or board[i][col] == 1:
                return False
        
        for i in range(-N, N):
            if 0 <= row + i < N and 0 <= col + i < N and board[row + i][col + i] == 1:
                return False
            if 0 <= row + i < N and 0 <= col - i < N and board[row + i][col - i] == 1:
                return False
        
        knight_moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
                       (1, -2), (1, 2), (2, -1), (2, 1)]
        
        for dr, dc in knight_moves:
            r, c = row + dr, col + dc
            if 0 <= r < N and 0 <= c < N and board[r][c] == 1:
                return False
        
        return True
    
    def backtrack(start_row, placed):
        nonlocal count
        if placed == K:
            count += 1
            return
        
        for i in range(start_row, N):
            for j in range(N):
                if can_place(i, j):
                    board[i][j] = 1
                    backtrack(i + 1, placed + 1)
                    board[i][j] = 0
    
    backtrack(0, 0)
    
    with open("OUTPUT.TXT", "w") as f:
        f.write(str(count))

if __name__ == "__main__":
    main()
