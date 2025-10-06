
import collections

def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    grid = []
    index = 1
    for i in range(n):
        row = list(map(int, data[index:index+n]))
        index += n
        grid.append(row)
    
    result = [[0] * n for _ in range(n)]
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    for i in range(n):
        for j in range(n):
            if grid[i][j] != 0:
                result[i][j] = grid[i][j]
                continue
                
            visited = [[False] * n for _ in range(n)]
            queue = collections.deque()
            queue.append((i, j, 0))
            visited[i][j] = True
            candidates = []
            min_dist = float('inf')
            
            while queue:
                x, y, dist = queue.popleft()
                
                if dist > min_dist:
                    break
                    
                if grid[x][y] != 0:
                    if dist < min_dist:
                        min_dist = dist
                        candidates = [grid[x][y]]
                    elif dist == min_dist:
                        candidates.append(grid[x][y])
                    continue
                    
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                        visited[nx][ny] = True
                        queue.append((nx, ny, dist + 1))
            
            if len(candidates) == 1:
                result[i][j] = candidates[0]
            else:
                result[i][j] = 0
                
    for i in range(n):
        print(' '.join(map(str, result[i])))

if __name__ == "__main__":
    main()
