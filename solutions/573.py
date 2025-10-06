
import math

def main():
    import sys
    data = sys.stdin.read().splitlines()
    n, v = map(int, data[0].split())
    events = []
    for i in range(1, n+1):
        parts = data[i].split()
        time_str = parts[0]
        x = int(parts[1])
        y = int(parts[2])
        h, m = map(int, time_str.split(':'))
        total_minutes = h * 60 + m
        events.append((total_minutes, x, y))
    
    events.sort(key=lambda x: x[0])
    
    graph = [[] for _ in range(n)]
    for i in range(n):
        t1, x1, y1 = events[i]
        for j in range(i+1, n):
            t2, x2, y2 = events[j]
            dt = (t2 - t1) / 60.0
            if dt == 0:
                continue
            dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
            required_speed = dist / dt
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
