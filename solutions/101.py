
def main():
    import sys
    sys.setrecursionlimit(10000)
    data = sys.stdin.read().split()
    if not data:
        return
    N = int(data[0])
    K = int(data[1])
    
    if K == 0:
        print(1)
        return
        
    board = [[0] * N for _ in range(N)]
    count = 0
    
    knight_moves = [(2, 1), (2, -1), (-2, 1), (-2, -1),
                   (1, 2), (1, -2), (-1, 2), (-1, -2)]
    
    def is_safe(row, col):
        for i in range(N):
            if board[row][i] == 1:
                return False
            if board[i][col] == 1:
                return False
            if row - i >= 0 and col - i >= 0 and board[row-i][col-i] == 1:
                return False
            if row - i >= 0 and col + i < N and board[row-i][col+i] == 1:
                return False
            if row + i < N and col - i >= 0 and board[row+i][col-i] == 1:
                return False
            if row + i < N and col + i < N and board[row+i][col+i] == 1:
                return False
                
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
                if is_safe(i, j):
                    board[i][j] = 1
                    backtrack(i + 1, placed + 1)
                    board[i][j] = 0
                    
    backtrack(0, 0)
    print(count)

if __name__ == "__main__":
    main()
