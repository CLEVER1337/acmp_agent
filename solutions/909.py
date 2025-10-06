
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
    
    def dfs(x, y):
        stack = [(x, y)]
        visited[x][y] = True
        has_s = False
        has_x = False
        
        while stack:
            cx, cy = stack.pop()
            if grid[cx][cy] == 'S':
                has_s = True
            elif grid[cx][cy] == 'X':
                has_x = True
                
            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and grid[nx][ny] in ['S', 'X']:
                    visited[nx][ny] = True
                    stack.append((nx, ny))
                    
        return has_s, has_x
    
    whole_ships = 0
    damaged_ships = 0
    destroyed_ships = 0
    
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and grid[i][j] in ['S', 'X']:
                has_s, has_x = dfs(i, j)
                if has_s and not has_x:
                    whole_ships += 1
                elif has_s and has_x:
                    damaged_ships += 1
                elif not has_s and has_x:
                    destroyed_ships += 1
                    
    print(f"{whole_ships} {damaged_ships} {destroyed_ships}")

if __name__ == "__main__":
    main()
