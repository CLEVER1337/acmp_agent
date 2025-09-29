
import heapq

def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        print("IMPOSSIBLE")
        return
        
    idx = 0
    n = int(data[idx]); m = int(data[idx+1]); idx += 2
    X = int(data[idx]); Y = int(data[idx+1]); idx += 2
    X -= 1; Y -= 1
    K = int(data[idx]); D = int(data[idx+1]); idx += 2
    
    grid = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(int(data[idx])); idx += 1
        grid.append(row)
    
    if grid[0][0] == 0:
        print("IMPOSSIBLE")
        return
        
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    INF = float('inf')
    dist = [[[INF] * (K + 1) for _ in range(n)] for _ in range(m)]
    dist[0][0][K] = 0
    
    pq = []
    heapq.heappush(pq, (0, 0, 0, K))
    
    while pq:
        actions, x, y, k_left = heapq.heappop(pq)
        
        if x == X and y == Y:
            print(actions)
            return
            
        if actions > dist[x][y][k_left]:
            continue
            
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n:
                if grid[nx][ny] == 0:
                    continue
                if abs(grid[nx][ny] - grid[x][y]) <= 1:
                    new_actions = actions + 1
                    if new_actions < dist[nx][ny][k_left]:
                        dist[nx][ny][k_left] = new_actions
                        heapq.heappush(pq, (new_actions, nx, ny, k_left))
        
        if k_left > 0:
            for dx, dy in directions:
                for dist_move in range(1, D + 1):
                    nx, ny = x + dx * dist_move, y + dy * dist_move
                    if not (0 <= nx < m and 0 <= ny < n):
                        continue
                    
                    if grid[nx][ny] == 0:
                        continue
                    
                    height_diff = abs(grid[nx][ny] - grid[x][y])
                    energy_needed = dist_move + height_diff
                    
                    if energy_needed <= D:
                        new_k = k_left - 1
                        new_actions = actions + 1
                        if new_actions < dist[nx][ny][new_k]:
                            dist[nx][ny][new_k] = new_actions
                            heapq.heappush(pq, (new_actions, nx, ny, new_k))
    
    min_actions = min(dist[X][Y])
    if min_actions != INF:
        print(min_actions)
    else:
        print("IMPOSSIBLE")

if __name__ == "__main__":
    main()
