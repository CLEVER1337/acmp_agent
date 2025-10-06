
def main():
    import sys
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    grid = []
    cities = []
    for i in range(1, n+1):
        line = data[i].strip()
        grid.append(line)
        for j in range(n):
            if line[j] == 'C':
                cities.append((i-1, j))
    
    total_cities = len(cities)
    half = total_cities // 2
    
    state = [[0] * n for _ in range(n)]
    count1 = 0
    
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'C':
                if count1 < half:
                    state[i][j] = 1
                    count1 += 1
                else:
                    state[i][j] = 2
    
    visited = [[False] * n for _ in range(n)]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    def dfs(i, j, target):
        stack = [(i, j)]
        visited[i][j] = True
        while stack:
            x, y = stack.pop()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                    if state[nx][ny] == target:
                        visited[nx][ny] = True
                        stack.append((nx, ny))
    
    components = []
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                components.append((i, j, state[i][j]))
                dfs(i, j, state[i][j])
    
    comp_map = {}
    for idx, (i, j, s) in enumerate(components):
        comp_map[(i, j)] = idx
    
    comp_adj = [[] for _ in range(len(components))]
    for i in range(n):
        for j in range(n):
            comp_id = comp_map[(i, j)]
            for dx, dy in directions:
                ni, nj = i + dx, j + dy
                if 0 <= ni < n and 0 <= nj < n:
                    neighbor_comp = comp_map[(ni, nj)]
                    if neighbor_comp != comp_id:
                        comp_adj[comp_id].append(neighbor_comp)
    
    comp_size = [0] * len(components)
    comp_state = [0] * len(components)
    for i in range(n):
        for j in range(n):
            comp_id = comp_map[(i, j)]
            comp_size[comp_id] += 1
            comp_state[comp_id] = state[i][j]
    
    def can_merge(comp1, comp2):
        return comp_state[comp1] == comp_state[comp2]
    
    merged = True
    while merged:
        merged = False
        for comp_id in range(len(components)):
            for neighbor in comp_adj[comp_id]:
                if can_merge(comp_id, neighbor):
                    new_state = comp_state[comp_id]
                    for i in range(n):
                        for j in range(n):
                            if comp_map[(i, j)] == neighbor:
                                comp_map[(i, j)] = comp_id
                                state[i][j] = new_state
                    comp_adj[comp_id].extend(comp_adj[neighbor])
                    comp_adj[comp_id] = [x for x in comp_adj[comp_id] if x != comp_id]
                    comp_size[comp_id] += comp_size[neighbor]
                    comp_adj[neighbor] = []
                    merged = True
                    break
            if merged:
                break
    
    output_lines = []
    for i in range(n):
        output_lines.append(''.join(str(x) for x in state[i]))
    
    print('\n'.join(output_lines))

if __name__ == "__main__":
    main()
