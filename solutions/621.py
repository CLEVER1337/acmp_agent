
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    matrix = []
    index = 1
    for i in range(n):
        row = list(map(int, data[index:index+n]))
        index += n
        matrix.append(row)
    
    result = [row[:] for row in matrix]
    
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 0:
                visited = [[False] * n for _ in range(n)]
                queue = deque()
                queue.append((i, j, 0))
                visited[i][j] = True
                candidates = []
                min_dist = float('inf')
                
                while queue:
                    x, y, dist = queue.popleft()
                    
                    if dist > min_dist:
                        break
                        
                    if matrix[x][y] != 0:
                        if dist < min_dist:
                            min_dist = dist
                            candidates = [matrix[x][y]]
                        elif dist == min_dist:
                            candidates.append(matrix[x][y])
                        continue
                    
                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                            visited[nx][ny] = True
                            queue.append((nx, ny, dist + 1))
                
                if len(candidates) == 1:
                    result[i][j] = candidates[0]
    
    for i in range(n):
        print(' '.join(map(str, result[i])))

if __name__ == "__main__":
    main()
