
def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0]); k = int(data[1]); m = int(data[2])
    edges = []
    index = 3
    graph = [[] for _ in range(n+1)]
    for i in range(m):
        u = int(data[index]); v = int(data[index+1]); index += 2
        edges.append((u, v))
        graph[u].append(v)
        graph[v].append(u)
    
    adj = [[0]*(n+1) for _ in range(n+1)]
    for u, v in edges:
        adj[u][v] = 1
        adj[v][u] = 1
    
    best_team = None
    max_cohesion = -1
    
    from itertools import combinations
    all_nodes = list(range(1, n+1))
    
    for team1 in combinations(all_nodes, k):
        team1_set = set(team1)
        team2_set = set(all_nodes) - team1_set
        
        cohesion1 = 0
        for i in team1_set:
            for j in team1_set:
                if i < j and adj[i][j]:
                    cohesion1 += 1
        
        cohesion2 = 0
        for i in team2_set:
            for j in team2_set:
                if i < j and adj[i][j]:
                    cohesion2 += 1
        
        total = cohesion1 + cohesion2
        if total > max_cohesion:
            max_cohesion = total
            best_team = sorted(team1)
    
    print(' '.join(map(str, best_team)))

if __name__ == "__main__":
    main()
