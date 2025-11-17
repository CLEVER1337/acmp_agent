
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    if not data:
        print(-1)
        return
        
    idx = 0
    N = int(data[idx]); M = int(data[idx+1]); idx += 2
    R = list(map(int, data[idx:idx+N])); idx += N
    C = list(map(int, data[idx:idx+M])); idx += M
    Z = []
    for i in range(N):
        row = list(map(int, data[idx:idx+M]))
        idx += M
        Z.append(row)
        
    total_fixed = 0
    fixed_entries = []
    row_fixed_sum = [0] * N
    col_fixed_sum = [0] * M
    for i in range(N):
        for j in range(M):
            if Z[i][j] != -1:
                total_fixed += Z[i][j]
                row_fixed_sum[i] += Z[i][j]
                col_fixed_sum[j] += Z[i][j]
                fixed_entries.append((i, j, Z[i][j]))
                
    for i in range(N):
        if row_fixed_sum[i] > R[i]:
            print(-1)
            return
            
    for j in range(M):
        if col_fixed_sum[j] > C[j]:
            print(-1)
            return
            
    n = N + M + 2
    s = 0
    t = n - 1
    graph = [[] for _ in range(n)]
    row_nodes = list(range(1, N+1))
    col_nodes = list(range(N+1, N+M+1))
    
    for i in range(N):
        cap = R[i] - row_fixed_sum[i]
        graph[s].append((row_nodes[i], cap))
        graph[row_nodes[i]].append((s, 0))
        
    for j in range(M):
        cap = C[j] - col_fixed_sum[j]
        graph[col_nodes[j]].append((t, cap))
        graph[t].append((col_nodes[j], 0))
        
    for i in range(N):
        for j in range(M):
            if Z[i][j] == -1:
                graph[row_nodes[i]].append((col_nodes[j], float('inf')))
                graph[col_nodes[j]].append((row_nodes[i], 0))
                
    def bfs():
        parent = [-1] * n
        min_cap = [0] * n
        min_cap[s] = float('inf')
        q = deque([s])
        while q:
            u = q.popleft()
            for edge in graph[u]:
                v, cap = edge
                if cap > 0 and parent[v] == -1:
                    parent[v] = u
                    min_cap[v] = min(min_cap[u], cap)
                    if v == t:
                        return parent, min_cap[t]
                    q.append(v)
        return None, 0
        
    max_flow = 0
    while True:
        parent, flow = bfs()
        if flow == 0:
            break
        max_flow += flow
        v = t
        while v != s:
            u = parent[v]
            for i in range(len(graph[u])):
                if graph[u][i][0] == v:
                    graph[u][i] = (v, graph[u][i][1] - flow)
                    break
            for i in range(len(graph[v])):
                if graph[v][i][0] == u:
                    graph[v][i] = (u, graph[v][i][1] + flow)
                    break
            v = u
            
    total = total_fixed + max_flow
    print(total)

if __name__ == "__main__":
    main()
