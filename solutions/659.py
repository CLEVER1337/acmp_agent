
import sys
from itertools import combinations

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    k = int(data[1])
    m = int(data[2])
    
    graph = [[False] * (n + 1) for _ in range(n + 1)]
    
    index = 3
    for i in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        index += 2
        graph[u][v] = True
        graph[v][u] = True
    
    all_nodes = list(range(1, n + 1))
    best_team = None
    max_cohesion = -1
    
    for team1 in combinations(all_nodes, k):
        team1_set = set(team1)
        team2_set = set(all_nodes) - team1_set
        
        cohesion1 = 0
        for u, v in combinations(team1, 2):
            if graph[u][v]:
                cohesion1 += 1
                
        cohesion2 = 0
        for u, v in combinations(team2_set, 2):
            if graph[u][v]:
                cohesion2 += 1
                
        total_cohesion = cohesion1 + cohesion2
        
        if total_cohesion > max_cohesion:
            max_cohesion = total_cohesion
            best_team = team1
    
    if best_team:
        print(" ".join(map(str, sorted(best_team))))

if __name__ == "__main__":
    main()
