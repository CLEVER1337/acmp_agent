
import heapq

def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        print("IMPOSSIBLE")
        return
        
    idx = 0
    M = int(data[idx]); N = int(data[idx+1]); idx += 2
    X = int(data[idx]); Y = int(data[idx+1]); idx += 2
    K = int(data[idx]); D = int(data[idx+1]); idx += 2
    
    grid = []
    for i in range(M):
        row = list(map(int, data[idx:idx+N]))
        idx += N
        grid.append(row)
    
    target = (X-1, Y-1)
    start = (0, 0)
    
    if grid[0][0] == 0 or grid[target[0]][target[1]] == 0:
        print("IMPOSSIBLE")
        return
        
    directions = [(0,1), (1,0), (0,-1), (-1,0)]
    
    INF = 10**9
    dist = [[[INF] * (K+1) for _ in range(N)] for _ in range(M)]
    dist[0][0][K] = 0
    
    pq = []
    heapq.heappush(pq, (0, 0, 0, K))
    
    while pq:
        actions, i, j, k = heapq.heappop(pq)
        
        if (i, j) == target:
            print(actions)
            return
            
        if actions > dist[i][j][k]:
            continue
            
        for dx, dy in directions:
            ni, nj = i + dx, j + dy
            if 0 <= ni < M and 0 <= nj < N:
                if grid[ni][nj] == 0:
                    continue
                if abs(grid[ni][nj] - grid[i][j]) <= 1:
                    new_actions = actions + 1
                    if new_actions < dist[ni][nj][k]:
                        dist[ni][nj][k] = new_actions
                        heapq.heappush(pq, (new_actions, ni, nj, k))
        
        if k > 0:
            for dx, dy in directions:
                for dist_move in range(1, D+1):
                    ni, nj = i + dx * dist_move, j + dy * dist_move
                    if not (0 <= ni < M and 0 <= nj < N):
                        break
                    if grid[ni][nj] == 0:
                        continue
                    
                    energy_needed = dist_move
                    height_diff = abs(grid[ni][nj] - grid[i][j])
                    if height_diff > dist_move:
                        continue
                    
                    energy_needed += height_diff
                    
                    if energy_needed <= D:
                        new_actions = actions + 1
                        new_k = k - 1
                        if new_actions < dist[ni][nj][new_k]:
                            dist[ni][nj][new_k] = new_actions
                            heapq.heappush(pq, (new_actions, ni, nj, new_k))
    
    min_actions = min(dist[target[0]][target[1]])
    if min_actions == INF:
        print("IMPOSSIBLE")
    else:
        print(min_actions)

if __name__ == "__main__":
    main()
