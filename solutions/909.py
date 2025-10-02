
import sys
sys.setrecursionlimit(1000000)

def main():
    data = sys.stdin.read().splitlines()
    if not data:
        print("0 0 0")
        return
        
    n, m = map(int, data[0].split())
    grid = []
    for i in range(1, 1 + n):
        grid.append(list(data[i]))
    
    visited = [[False] * m for _ in range(n)]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    whole_ships = 0
    damaged_ships = 0
    destroyed_ships = 0
    
    def dfs(i, j):
        stack = [(i, j)]
        visited[i][j] = True
        has_damaged = False
        has_whole = False
        
        while stack:
            x, y = stack.pop()
            if grid[x][y] == 'X':
                has_damaged = True
            elif grid[x][y] == 'S':
                has_whole = True
                
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and grid[nx][ny] in ['X', 'S']:
                    visited[nx][ny] = True
                    stack.append((nx, ny))
        
        return has_whole, has_damaged
    
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and grid[i][j] in ['X', 'S']:
                has_whole, has_damaged = dfs(i, j)
                if has_whole and not has_damaged:
                    whole_ships += 1
                elif has_damaged and not has_whole:
                    destroyed_ships += 1
                else:
                    damaged_ships += 1
                    
    print(f"{whole_ships} {damaged_ships} {destroyed_ships}")

if __name__ == "__main__":
    main()
