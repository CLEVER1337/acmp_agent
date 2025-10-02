
import sys
from itertools import combinations

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    m = int(data[1])
    
    edges = []
    index = 2
    graph = [[] for _ in range(n+1)]
    for i in range(m):
        u = int(data[index])
        v = int(data[index+1])
        index += 2
        edges.append((u, v))
        graph[u].append(v)
        graph[v].append(u)
    
    min_k = n
    count = 0
    best_set = None
    
    for k in range(1, n+1):
        found = False
        for combo in combinations(range(1, n+1), k):
            covered_edges = set()
            for station in combo:
                for neighbor in graph[station]:
                    edge = tuple(sorted((station, neighbor)))
                    covered_edges.add(edge)
            
            if len(covered_edges) == m:
                if k < min_k:
                    min_k = k
                    count = 1
                    best_set = combo
                    found = True
                elif k == min_k:
                    count += 1
                    if best_set is None:
                        best_set = combo
        
        if found:
            break
    
    if min_k == n and count == 0:
        min_k = n
        count = 1
        best_set = tuple(range(1, n+1))
    
    print(f"{min_k} {count}")
    if best_set:
        print(" ".join(map(str, best_set)))

if __name__ == "__main__":
    main()
