
def main():
    import sys
    sys.setrecursionlimit(10000)
    data = sys.stdin.read().split()
    N = int(data[0])
    K = int(data[1])
    
    if K == 0:
        print(1)
        return
        
    board = [[False] * N for _ in range(N)]
    count = 0
    
    def is_safe(row, col):
        for i in range(N):
            if board[i][col]:
                return False
                
        for j in range(N):
            if board[row][j]:
                return False
                
        i, j = row, col
        while i >= 0 and j >= 0:
            if board[i][j]:
                return False
            i -= 1
            j -= 1
            
        i, j = row, col
        while i < N and j < N:
            if board[i][j]:
                return False
            i += 1
            j += 1
            
        i, j = row, col
        while i >= 0 and j < N:
            if board[i][j]:
                return False
            i -= 1
            j += 1
            
        i, j = row, col
        while i < N and j >= 0:
            if board[i][j]:
                return False
            i += 1
            j -= 1
            
        knight_moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
                       (1, -2), (1, 2), (2, -1), (2, 1)]
        for dr, dc in knight_moves:
            r, c = row + dr, col + dc
            if 0 <= r < N and 0 <= c < N and board[r][c]:
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
                    board[i][j] = True
                    backtrack(i + 1, placed + 1)
                    board[i][j] = False
                    
    backtrack(0, 0)
    print(count)

if __name__ == "__main__":
    main()
