
def main():
    import sys
    sys.setrecursionlimit(10000)
    
    def dfs(i, j, visited, board, n, color):
        if i < 0 or i >= n or j < 0 or j >= n or visited[i][j] or board[i][j] != color:
            return set()
        visited[i][j] = True
        group_dame = set()
        for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
            ni, nj = i + dx, j + dy
            if 0 <= ni < n and 0 <= nj < n:
                if board[ni][nj] == '.':
                    group_dame.add((ni, nj))
                elif board[ni][nj] == color:
                    subgroup_dame = dfs(ni, nj, visited, board, n, color)
                    group_dame.update(subgroup_dame)
        return group_dame

    data = sys.stdin.read().splitlines()
    n = int(data[0])
    board = []
    for i in range(1, n+1):
        board.append(list(data[i].strip()))
    
    visited = [[False]*n for _ in range(n)]
    atari_count = 0
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == 'B' and not visited[i][j]:
                dame_set = dfs(i, j, visited, board, n, 'B')
                if len(dame_set) == 1:
                    atari_count += 1
                    
    print(atari_count)

if __name__ == "__main__":
    main()
