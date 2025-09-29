
import sys
sys.setrecursionlimit(100000)

def main():
    data = sys.stdin.read().split()
    if not data:
        print(0)
        return
        
    n = int(data[0])
    m = int(data[1])
    grid = []
    index = 2
    for i in range(n):
        row = []
        for j in range(m):
            row.append(int(data[index]))
            index += 1
        grid.append(row)
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    def get_neighbors(i, j):
        neighbors = []
        for dx, dy in directions:
            ni, nj = i + dx, j + dy
            if 0 <= ni < n and 0 <= nj < m:
                neighbors.append((ni, nj))
        return neighbors
    
    visited = [[False] * m for _ in range(n)]
    components = []
    
    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                stack = [(i, j)]
                component = []
                visited[i][j] = True
                
                while stack:
                    ci, cj = stack.pop()
                    component.append((ci, cj))
                    
                    for ni, nj in get_neighbors(ci, cj):
                        if not visited[ni][nj] and grid[ni][nj] == grid[ci][cj]:
                            visited[ni][nj] = True
                            stack.append((ni, nj))
                
                components.append(component)
    
    def is_sink(component):
        for i, j in component:
            for ni, nj in get_neighbors(i, j):
                if grid[ni][nj] < grid[i][j]:
                    return True
        return False
    
    count = 0
    for component in components:
        if not is_sink(component):
            count += 1
            
    print(count)

if __name__ == "__main__":
    main()
