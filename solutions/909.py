
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
        grid.append(list(data[i].strip()))
    
    visited = [[False] * m for _ in range(n)]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    def dfs(i, j, ship_cells):
        if i < 0 or i >= n or j < 0 or j >= m or visited[i][j]:
            return
        if grid[i][j] not in ['X', 'S']:
            return
            
        visited[i][j] = True
        ship_cells.append((i, j))
        
        for dx, dy in directions:
            dfs(i + dx, j + dy, ship_cells)
    
    destroyed = 0
    damaged = 0
    intact = 0
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] in ['X', 'S'] and not visited[i][j]:
                ship_cells = []
                dfs(i, j, ship_cells)
                
                has_intact = any(grid[x][y] == 'S' for x, y in ship_cells)
                has_damaged = any(grid[x][y] == 'X' for x, y in ship_cells)
                
                if has_intact and has_damaged:
                    damaged += 1
                elif has_intact:
                    intact += 1
                elif has_damaged:
                    destroyed += 1
    
    print(f"{intact} {damaged} {destroyed}")

if __name__ == "__main__":
    main()
