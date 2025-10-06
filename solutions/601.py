
import sys
from collections import defaultdict, deque

def main():
    data = sys.stdin.read().split()
    if not data:
        print("INCORRECT")
        return
        
    it = iter(data)
    n = int(next(it)); m = int(next(it))
    
    graph = defaultdict(dict)
    
    for _ in range(m):
        u = int(next(it)); v = int(next(it)); c = int(next(it))
        if c not in graph[u]:
            graph[u][c] = []
        graph[u][c].append(v)
        
        if c not in graph[v]:
            graph[v][c] = []
        graph[v][c].append(u)
    
    k = int(next(it))
    colors = []
    for _ in range(k):
        colors.append(int(next(it)))
    
    current = 1
    for i, c in enumerate(colors):
        if c not in graph[current] or not graph[current][c]:
            print("INCORRECT")
            return
        current = graph[current][c][0]
    
    print(current)

if __name__ == "__main__":
    main()
