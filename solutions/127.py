
from collections import deque

def main():
    with open('INPUT.TXT', 'r') as f:
        n = int(f.readline().strip())
        graph = []
        for _ in range(n):
            row = list(map(int, f.readline().split()))
            graph.append(row)
        start, end = map(int, f.readline().split())
        start -= 1
        end -= 1
        
        if start == end:
            with open('OUTPUT.TXT', 'w') as out:
                out.write('0')
            return
        
        visited = [False] * n
        distance = [-1] * n
        queue = deque()
        
        visited[start] = True
        distance[start] = 0
        queue.append(start)
        
        while queue:
            current = queue.popleft()
            
            for neighbor in range(n):
                if graph[current][neighbor] == 1 and not visited[neighbor]:
                    visited[neighbor] = True
                    distance[neighbor] = distance[current] + 1
                    queue.append(neighbor)
                    
                    if neighbor == end:
                        with open('OUTPUT.TXT', 'w') as out:
                            out.write(str(distance[neighbor]))
                        return
        
        with open('OUTPUT.TXT', 'w') as out:
            out.write('-1')

if __name__ == "__main__":
    main()
