
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
        a = int(data[index])
        b = int(data[index+1])
        c = int(data[index+2])
        index += 3
        edges.append((a, b, c, i+1))
    
    boys = n
    girls = m
    total_nodes = boys + girls + 2
    source = 0
    sink = total_nodes - 1
    
    from collections import deque
    INF = 10**9
    
    graph = [[] for _ in range(total_nodes)]
    
    for idx, (a, b, c, num) in enumerate(edges):
        u = a
        v = boys + b
        graph[u].append((v, c, idx, len(graph[v])))
        graph[v].append((u, -c, idx, len(graph[u])-1))
    
    for i in range(1, boys+1):
        graph[source].append((i, 0, -1, len(graph[i])))
        graph[i].append((source, 0, -1, len(graph[source])-1))
    
    for j in range(1, girls+1):
        node_j = boys + j
        graph[node_j].append((sink, 0, -1, len(graph[sink])))
        graph[sink].append((node_j, 0, -1, len(graph[node_j])-1))
    
    dist = [INF] * total_nodes
    parent = [-1] * total_nodes
    parent_edge = [-1] * total_nodes
    in_queue = [False] * total_nodes
    dist[source] = 0
    q = deque([source])
    in_queue[source] = True
    
    while q:
        u = q.popleft()
        in_queue[u] = False
        for idx, (v, cost, edge_idx, rev_idx) in enumerate(graph[u]):
            if dist[u] + cost < dist[v]:
                dist[v] = dist[u] + cost
                parent[v] = u
                parent_edge[v] = idx
                if not in_queue[v]:
                    in_queue[v] = True
                    q.append(v)
    
    if dist[sink] == INF:
        print(-1)
        return
    
    total_cost = 0
    selected_edges = []
    flow = 0
    u = sink
    path_edges = []
    while u != source:
        p = parent[u]
        edge_index = parent_edge[u]
        edge_info = graph[p][edge_index]
        v, cost, edge_idx, rev_idx = edge_info
        if edge_idx != -1:
            path_edges.append(edge_idx)
        total_cost += cost
        u = p
    
    selected_edges.extend(path_edges)
    k = len(selected_edges)
    
    print(total_cost)
    print(k)
    if k > 0:
        print(" ".join(map(str, selected_edges)))
    else:
        print()

if __name__ == "__main__":
    main()
