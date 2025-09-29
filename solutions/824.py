
def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        print(0)
        return
        
    n = int(data[0])
    m = int(data[1])
    edges = []
    index = 2
    for i in range(m):
        u = int(data[index]); v = int(data[index+1]); index += 2
        edges.append((min(u, v), max(u, v)))
    
    from collections import defaultdict
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    visited = [False] * (n + 1)
    components = 0
    for i in range(1, n + 1):
        if not visited[i]:
            components += 1
            stack = [i]
            visited[i] = True
            while stack:
                node = stack.pop()
                for neighbor in graph[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        stack.append(neighbor)
    
    if components > 1:
        print(0)
        return
        
    total_edges = m
    required_edges = n - 1
    
    if total_edges < required_edges:
        print(0)
        return
        
    from math import comb
    result = comb(total_edges, required_edges)
    print(result)

if __name__ == "__main__":
    main()
