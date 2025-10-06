
import sys

def main():
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
    
    graph = [[] for _ in range(total_nodes)]
    edge_info = {}
    
    for idx, (a, b, c, orig_idx) in enumerate(edges):
        u = a
        v = boys + b
        graph[u].append((v, c, idx*2))
        graph[v].append((u, 0, idx*2+1))
        edge_info[idx*2] = (u, v, c, orig_idx)
        edge_info[idx*2+1] = (v, u, 0, orig_idx)
    
    for i in range(1, boys+1):
        graph[source].append((i, 0, len(edge_info)))
        graph[i].append((source, 0, len(edge_info)+1))
        edge_info[len(edge_info)] = (source, i, 0, -1)
        edge_info[len(edge_info)] = (i, source, 0, -1)
    
    for i in range(boys+1, boys+girls+1):
        graph[i].append((sink, 0, len(edge_info)))
        graph[sink].append((i, 0, len(edge_info)+1))
        edge_info[len(edge_info)] = (i, sink, 0, -1)
        edge_info[len(edge_info)] = (sink, i, 0, -1)
    
    def bellman_ford():
        dist = [float('inf')] * total_nodes
        parent = [-1] * total_nodes
        dist[source] = 0
        for _ in range(total_nodes - 1):
            updated = False
            for u in range(total_nodes):
                if dist[u] == float('inf'):
                    continue
                for edge in graph[u]:
                    v, cost, idx = edge
                    if dist[u] + cost < dist[v]:
                        dist[v] = dist[u] + cost
                        parent[v] = (u, idx)
                        updated = True
            if not updated:
                break
        return dist, parent
    
    total_cost = 0
    selected_edges = set()
    
    while True:
        dist, parent = bellman_ford()
        if dist[sink] == float('inf'):
            break
        
        path = []
        cur = sink
        while cur != source:
            u, idx = parent[cur]
            path.append(idx)
            cur = u
        
        min_flow = float('inf')
        for idx in path:
            u, v, cap, orig_idx = edge_info[idx]
            if cap < min_flow:
                min_flow = cap
        
        for idx in path:
            u, v, cap, orig_idx = edge_info[idx]
            if orig_idx != -1:
                if idx % 2 == 0:
                    selected_edges.add(orig_idx)
                else:
                    selected_edges.discard(orig_idx)
        
        total_cost += min_flow * dist[sink]
        
        for idx in path:
            u, v, cap, orig_idx = edge_info[idx]
            edge_info[idx] = (u, v, cap - min_flow, orig_idx)
            rev_idx = idx + 1 if idx % 2 == 0 else idx - 1
            u_rev, v_rev, cap_rev, orig_idx_rev = edge_info[rev_idx]
            edge_info[rev_idx] = (u_rev, v_rev, cap_rev + min_flow, orig_idx_rev)
    
    k = len(selected_edges)
    print(total_cost)
    print(k)
    if k > 0:
        print(' '.join(map(str, sorted(selected_edges))))
    else:
        print()

if __name__ == "__main__":
    main()
