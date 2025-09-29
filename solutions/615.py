
def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    m = int(data[1])
    r = int(data[2])
    edges = []
    index = 3
    for i in range(r):
        a = int(data[index]); b = int(data[index+1]); c = int(data[index+2])
        index += 3
        edges.append((a, b, c, i+1))
    
    boys = n
    girls = m
    size = boys + girls + 2
    source = 0
    sink = size - 1
    
    graph = [[] for _ in range(size)]
    capacities = [[0] * size for _ in range(size)]
    costs = [[0] * size for _ in range(size)]
    edge_indices = [[-1] * size for _ in range(size)]
    
    for i in range(1, boys+1):
        graph[source].append(i)
        graph[i].append(source)
        capacities[source][i] = 1
        costs[source][i] = 0
        costs[i][source] = 0
        
    for j in range(boys+1, boys+girls+1):
        graph[j].append(sink)
        graph[sink].append(j)
        capacities[j][sink] = 1
        costs[j][sink] = 0
        costs[sink][j] = 0
        
    for idx, (a, b, c, num) in enumerate(edges):
        u = a
        v = boys + b
        graph[u].append(v)
        graph[v].append(u)
        capacities[u][v] = 1
        costs[u][v] = c
        costs[v][u] = -c
        edge_indices[u][v] = num
        
    INF = 10**9
    total_cost = 0
    total_flow = 0
    parent = [-1] * size
    dist = [INF] * size
    
    while True:
        dist[source] = 0
        updated = True
        while updated:
            updated = False
            for u in range(size):
                if dist[u] == INF:
                    continue
                for v in graph[u]:
                    if capacities[u][v] > 0 and dist[v] > dist[u] + costs[u][v]:
                        dist[v] = dist[u] + costs[u][v]
                        parent[v] = u
                        updated = True
        if dist[sink] == INF:
            break
            
        flow = INF
        cur = sink
        while cur != source:
            prev = parent[cur]
            flow = min(flow, capacities[prev][cur])
            cur = prev
            
        cur = sink
        while cur != source:
            prev = parent[cur]
            capacities[prev][cur] -= flow
            capacities[cur][prev] += flow
            total_cost += flow * costs[prev][cur]
            cur = prev
            
        total_flow += flow
        dist = [INF] * size
        
    result_edges = []
    for u in range(1, boys+1):
        for v in range(boys+1, boys+girls+1):
            if capacities[v][u] > 0 and edge_indices[u][v] != -1:
                result_edges.append(edge_indices[u][v])
                
    print(total_cost)
    print(len(result_edges))
    print(' '.join(map(str, result_edges)))

if __name__ == "__main__":
    main()
