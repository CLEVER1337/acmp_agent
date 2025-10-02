
def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    k = int(data[1])
    m = int(data[2])
    
    graph = [[0] * (n+1) for _ in range(n+1)]
    
    idx = 3
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx+1])
        idx += 2
        graph[u][v] = 1
        graph[v][u] = 1
    
    best_team = None
    max_cohesion = -1
    
    from itertools import combinations
    
    for team1 in combinations(range(1, n+1), k):
        team1_set = set(team1)
        team2_set = set(range(1, n+1)) - team1_set
        
        cohesion1 = 0
        for i in team1_set:
            for j in team1_set:
                if i < j and graph[i][j]:
                    cohesion1 += 1
        
        cohesion2 = 0
        for i in team2_set:
            for j in team2_set:
                if i < j and graph[i][j]:
                    cohesion2 += 1
        
        total_cohesion = cohesion1 + cohesion2
        
        if total_cohesion > max_cohesion:
            max_cohesion = total_cohesion
            best_team = team1
    
    print(" ".join(map(str, best_team)))

if __name__ == "__main__":
    main()
