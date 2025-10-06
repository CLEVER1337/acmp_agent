
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    if not data:
        print("IMPOSSIBLE")
        return
        
    idx = 0
    M, N = int(data[idx]), int(data[idx+1]); idx += 2
    Y, X = int(data[idx]), int(data[idx+1]); idx += 2
    K, D = int(data[idx]), int(data[idx+1]); idx += 2
    
    grid = []
    for i in range(M):
        row = list(map(int, data[idx:idx+N]))
        idx += N
        grid.append(row)
    
    if grid[0][0] == 0 or grid[X-1][Y-1] == 0:
        print("IMPOSSIBLE")
        return
        
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    INF = 10**9
    dist = [[[INF] * (K+1) for _ in range(N)] for __ in range(M)]
    dist[0][0][K] = 0
    q = deque()
    q.append((0, 0, K, 0))
    
    while q:
        x, y, k, steps = q.popleft()
        if x == X-1 and y == Y-1:
            print(steps)
            return
            
        if steps > dist[x][y][k]:
            continue
            
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < M and 0 <= ny < N:
                if grid[nx][ny] == 0:
                    continue
                if abs(grid[nx][ny] - grid[x][y]) > 1:
                    continue
                if dist[nx][ny][k] > steps + 1:
                    dist[nx][ny][k] = steps + 1
                    q.append((nx, ny, k, steps + 1))
                    
        if k > 0:
            for dx, dy in directions:
                for d in range(1, D+1):
                    nx, ny = x + dx * d, y + dy * d
                    if not (0 <= nx < M and 0 <= ny < N):
                        break
                    if grid[nx][ny] == 0:
                        continue
                    energy_needed = 0
                    valid = True
                    for i in range(1, d+1):
                        cx, cy = x + dx * i, y + dy * i
                        if grid[cx][cy] == 0:
                            valid = False
                            break
                        prev_h = grid[x][y] if i == 1 else grid[x + dx*(i-1)][y + dy*(i-1)]
                        curr_h = grid[cx][cy]
                        energy_needed += abs(curr_h - prev_h)
                        if energy_needed > D:
                            valid = False
                            break
                    if not valid:
                        continue
                    if dist[nx][ny][k-1] > steps + 1:
                        dist[nx][ny][k-1] = steps + 1
                        q.append((nx, ny, k-1, steps + 1))
                        
    ans = INF
    for k in range(K+1):
        ans = min(ans, dist[X-1][Y-1][k])
        
    if ans == INF:
        print("IMPOSSIBLE")
    else:
        print(ans)

if __name__ == "__main__":
    main()
