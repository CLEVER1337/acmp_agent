
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    graph = [[] for _ in range(n + 1)]
    dependencies = [[] for _ in range(n + 1)]
    in_degree = [0] * (n + 1)
    
    index = 1
    for i in range(1, n + 1):
        line = []
        while index < len(data) and data[index] != '0':
            line.append(int(data[index]))
            index += 1
        index += 1
        
        for dep in line:
            graph[dep].append(i)
            dependencies[i].append(dep)
            in_degree[i] += 1
    
    required = [False] * (n + 1)
    required[1] = True
    queue = deque([1])
    
    while queue:
        node = queue.popleft()
        for dep in dependencies[node]:
            if not required[dep]:
                required[dep] = True
                queue.append(dep)
    
    new_graph = [[] for _ in range(n + 1)]
    new_in_degree = [0] * (n + 1)
    
    for i in range(1, n + 1):
        if required[i]:
            for dep in dependencies[i]:
                if required[dep]:
                    new_graph[dep].append(i)
                    new_in_degree[i] += 1
    
    queue = deque()
    for i in range(1, n + 1):
        if required[i] and new_in_degree[i] == 0:
            queue.append(i)
    
    result = []
    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in new_graph[node]:
            new_in_degree[neighbor] -= 1
            if new_in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    print(len(result))
    for theorem in result:
        print(theorem)

if __name__ == "__main__":
    main()
