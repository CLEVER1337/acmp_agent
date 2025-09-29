
def main():
    import sys
    data = sys.stdin.read().splitlines()
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
        t1, x1, y1 = observations[i]
        for j in range(i + 1, n):
            t2, x2, y2 = observations[j]
            dt = (t2 - t1) / 60.0
            if dt == 0:
                continue
                
            distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
            required_speed = distance / dt
            
            if required_speed <= v:
                graph[i].append(j)
                graph[j].append(i)
    
    visited = [False] * n
    count = 0
    
    for i in range(n):
        if not visited[i]:
            count += 1
            stack = [i]
            visited[i] = True
            while stack:
                node = stack.pop()
                for neighbor in graph[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        stack.append(neighbor)
    
    print(count)

if __name__ == "__main__":
    main()
