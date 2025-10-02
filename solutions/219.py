
import sys

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
    
    INF = 10**18
    
    n = N + M + 2
    source = 0
    sink = n - 1
    
    from collections import defaultdict
    graph = defaultdict(dict)
    
    for i in range(N):
        graph[source][i+1] = R[i]
        graph[i+1][source] = 0
        
    for j in range(M):
        graph[N+j+1][sink] = C[j]
        graph[sink][N+j+1] = 0
        
    total_fixed = 0
    for i in range(N):
        for j in range(M):
            if Z[i][j] != -1:
                total_fixed += Z[i][j]
                graph[i+1][N+j+1] = 0
                graph[N+j+1][i+1] = Z[i][j]
            else:
                graph[i+1][N+j+1] = INF
                graph[N+j+1][i+1] = 0
    
    def bfs(level):
        from collections import deque
        q = deque()
        q.append(source)
        level[source] = 0
        while q:
            u = q.popleft()
            for v, cap in graph[u].items():
                if cap > 0 and level[v] == -1:
                    level[v] = level[u] + 1
                    q.append(v)
        return level[sink] != -1
    
    def dfs(u, flow, level, ptr):
        if u == sink:
            return flow
        while ptr[u] < len(list(graph[u].keys())):
            v = list(graph[u].keys())[ptr[u]]
            cap = graph[u][v]
            if cap > 0 and level[v] == level[u] + 1:
                pushed = dfs(v, min(flow, cap), level, ptr)
                if pushed > 0:
                    graph[u][v] -= pushed
                    graph[v][u] += pushed
                    return pushed
            ptr[u] += 1
        return 0
    
    total_flow = 0
    while True:
        level = [-1] * n
        if not bfs(level):
            break
        ptr = [0] * n
        while True:
            flow = dfs(source, INF, level, ptr)
            if flow == 0:
                break
            total_flow += flow
    
    max_sum = total_flow + total_fixed
    
    for i in range(N):
        row_sum = 0
        for j in range(M):
            if Z[i][j] != -1:
                row_sum += Z[i][j]
            else:
                row_sum += graph[N+j+1][i+1]
        if row_sum > R[i]:
            print(-1)
            return
            
    for j in range(M):
        col_sum = 0
        for i in range(N):
            if Z[i][j] != -1:
                col_sum += Z[i][j]
            else:
                col_sum += graph[N+j+1][i+1]
        if col_sum > C[j]:
            print(-1)
            return
            
    print(max_sum)

if __name__ == "__main__":
    main()
