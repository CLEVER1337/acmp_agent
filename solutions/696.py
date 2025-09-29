
from collections import deque

def main():
    import sys
    data = sys.stdin.read().splitlines()
    if not data:
        print("Sleep")
        return
        
    R, C = map(int, data[0].split())
    costs = list(map(int, data[1].split()))
    color_to_cost = {'R': costs[0], 'G': costs[1], 'B': costs[2], 'Y': costs[3]}
    
    grid = []
    start = None
    end = None
    
    for i in range(2, 2 + R):
        line = data[i].strip()
        grid.append(line)
        if 'S' in line:
            start = (i - 2, line.index('S'))
        if 'E' in line:
            end = (i - 2, line.index('E'))
    
    if not start or not end:
        print("Sleep")
        return
        
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = [[[False] * 16 for _ in range(C)] for _ in range(R)]
    queue = deque()
    r0, c0 = start
    queue.append((r0, c0, 0, 0))
    visited[r0][c0][0] = True
    
    min_cost = float('inf')
    
    while queue:
        r, c, keys, cost = queue.popleft()
        
        if (r, c) == end:
            min_cost = min(min_cost, cost)
            continue
            
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C:
                cell = grid[nr][nc]
                if cell == 'X':
                    continue
                    
                new_keys = keys
                new_cost = cost
                
                if cell in color_to_cost:
                    color_bit = {'R': 1, 'G': 2, 'B': 4, 'Y': 8}[cell]
                    if not (keys & color_bit):
                        new_keys |= color_bit
                        new_cost += color_to_cost[cell]
                
                if not visited[nr][nc][new_keys] or new_cost < cost:
                    visited[nr][nc][new_keys] = True
                    queue.append((nr, nc, new_keys, new_cost))
    
    if min_cost != float('inf'):
        print(min_cost)
    else:
        print("Sleep")

if __name__ == "__main__":
    main()
