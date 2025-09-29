
from collections import deque

def main():
    with open('INPUT.TXT', 'r') as f:
        lines = f.read().splitlines()
    
    m = int(lines[0])
    graph = {}
    
    for i in range(1, m + 1):
        if not lines[i].strip():
            continue
        parts = lines[i].split('->')
        if len(parts) < 2:
            continue
        src = parts[0].strip()
        dest = parts[1].strip()
        if src not in graph:
            graph[src] = []
        graph[src].append(dest)
    
    start = lines[m + 1].strip()
    end = lines[m + 2].strip()
    
    if start == end:
        print(0)
        return
    
    visited = {}
    queue = deque([(start, 0)])
    visited[start] = True
    
    while queue:
        current, steps = queue.popleft()
        
        if current not in graph:
            continue
            
        for neighbor in graph[current]:
            if neighbor == end:
                print(steps + 1)
                return
            if neighbor not in visited:
                visited[neighbor] = True
                queue.append((neighbor, steps + 1))
    
    print(-1)

if __name__ == "__main__":
    main()
