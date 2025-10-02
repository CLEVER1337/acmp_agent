
def main():
    import sys
    data = sys.stdin.read().splitlines()
    if not data:
        print(0)
        return
        
    n, v = map(int, data[0].split())
    observations = []
    
    for i in range(1, n + 1):
        parts = data[i].split()
        time_str = parts[0]
        x = int(parts[1])
        y = int(parts[2])
        
        hours, minutes = map(int, time_str.split(':'))
        total_minutes = hours * 60 + minutes
        observations.append((total_minutes, x, y))
    
    observations.sort()
    
    graph = [[] for _ in range(n)]
    
    for i in range(n):
        time_i, x_i, y_i = observations[i]
        for j in range(i + 1, n):
            time_j, x_j, y_j = observations[j]
            time_diff_hours = (time_j - time_i) / 60.0
            
            if time_diff_hours <= 0:
                continue
                
            distance = ((x_j - x_i)**2 + (y_j - y_i)**2)**0.5
            required_speed = distance / time_diff_hours
            
            if required_speed <= v:
                graph[i].append(j)
                graph[j].append(i)
    
    def dfs(u, visited):
        stack = [u]
        visited[u] = True
        while stack:
            node = stack.pop()
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    stack.append(neighbor)
    
    visited = [False] * n
    components = 0
    
    for i in range(n):
        if not visited[i]:
            components += 1
            dfs(i, visited)
    
    print(components)

if __name__ == "__main__":
    main()
