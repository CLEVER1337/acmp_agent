
from collections import deque

def main():
    with open('INPUT.TXT', 'r') as f:
        data = list(map(int, f.read().split()))
    
    n, x1, y1, x2, y2 = data
    x1 -= 1; y1 -= 1; x2 -= 1; y2 -= 1
    
    moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), 
             (1, -2), (1, 2), (2, -1), (2, 1)]
    
    visited = [[-1] * n for _ in range(n)]
    queue = deque()
    queue.append((x1, y1))
    visited[x1][y1] = 0
    
    while queue:
        x, y = queue.popleft()
        if x == x2 and y == y2:
            break
            
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(visited[x2][y2]))

if __name__ == "__main__":
    main()
