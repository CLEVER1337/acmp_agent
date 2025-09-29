
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
    for i in range(m):
        u = int(data[index]); v = int(data[index+1]); index += 2
        edges.append((u-1, v-1))
    
    min_vertex_cover = n
    count_ways = 0
    best_solution = []
    
    for k in range(1, n+1):
        found = False
        for combo in combinations(range(n), k):
            covers_all = True
            for u, v in edges:
                if u not in combo and v not in combo:
                    covers_all = False
                    break
            
            if covers_all:
                if k < min_vertex_cover:
                    min_vertex_cover = k
                    count_ways = 1
                    best_solution = list(combo)
                    found = True
                elif k == min_vertex_cover:
                    count_ways += 1
                    if not best_solution:
                        best_solution = list(combo)
        
        if found:
            break
    
    best_solution = [x+1 for x in best_solution]
    print(f"{min_vertex_cover} {count_ways}")
    print(" ".join(map(str, best_solution)))

if __name__ == "__main__":
    main()
