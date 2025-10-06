
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        print(-1)
        return
        
    idx = 0
    n = int(data[idx]); m = int(data[idx+1]); idx += 2
    R = list(map(int, data[idx:idx+n])); idx += n
    C = list(map(int, data[idx:idx+m])); idx += m
    
    Z = []
    for i in range(n):
        row = list(map(int, data[idx:idx+m]))
        idx += m
        Z.append(row)
    
    total_sum = 0
    fixed_sum = 0
    row_sums = [0] * n
    col_sums = [0] * m
    
    for i in range(n):
        for j in range(m):
            if Z[i][j] != -1:
                fixed_sum += Z[i][j]
                row_sums[i] += Z[i][j]
                col_sums[j] += Z[i][j]
    
    INF = 10**18
    from collections import deque
    
    class FlowGraph:
        def __init__(self, n):
            self.n = n
            self.graph = [[] for _ in range(n)]
            self.cap = []
            self.flow = []
            
        def add_edge(self, u, v, cap):
            idx1 = len(self.graph[u])
            idx2 = len(self.graph[v])
            self.graph[u].append((v, idx2))
            self.graph[v].append((u, idx1))
            self.cap.append(cap)
            self.cap.append(0)
            self.flow.append(0)
            self.flow.append(0)
            
        def bfs(self, s, t):
            dist = [-1] * self.n
            dist[s] = 0
            q = deque([s])
            while q:
                u = q.popleft()
                for idx, (v, rev_idx) in enumerate(self.graph[u]):
                    if dist[v] == -1 and self.flow[self.get_edge_idx(u, idx)] < self.cap[self.get_edge_idx(u, idx)]:
                        dist[v] = dist[u] + 1
                        q.append(v)
            return dist[t] != -1
            
        def get_edge_idx(self, u, idx):
            start_idx = sum(len(self.graph[i]) for i in range(u)) + idx
            return start_idx
            
        def dfs(self, u, t, f):
            if u == t:
                return f
            for idx, (v, rev_idx) in enumerate(self.graph[u]):
                edge_idx = self.get_edge_idx(u, idx)
                if self.flow[edge_idx] < self.cap[edge_idx]:
                    if v != u:
                        pushed = self.dfs(v, t, min(f, self.cap[edge_idx] - self.flow[edge_idx]))
                        if pushed > 0:
                            self.flow[edge_idx] += pushed
                            rev_edge_idx = self.get_edge_idx(v, rev_idx)
                            self.flow[rev_edge_idx] -= pushed
                            return pushed
            return 0
            
        def max_flow(self, s, t):
            total_flow = 0
            while self.bfs(s, t):
                while True:
                    f = self.dfs(s, t, INF)
                    if f == 0:
                        break
                    total_flow += f
            return total_flow
    
    s = n + m
    t = s + 1
    graph = FlowGraph(n + m + 2)
    
    for i in range(n):
        graph.add_edge(s, i, R[i] - row_sums[i])
        
    for j in range(m):
        graph.add_edge(n + j, t, C[j] - col_sums[j])
        
    for i in range(n):
        for j in range(m):
            if Z[i][j] == -1:
                graph.add_edge(i, n + j, INF)
                
    max_flow = graph.max_flow(s, t)
    
    total_free = 0
    for i in range(n):
        total_free += R[i] - row_sums[i]
        
    if total_free != max_flow:
        print(-1)
        return
        
    result = fixed_sum
    for i in range(n):
        for j in range(m):
            if Z[i][j] == -1:
                edge_idx = None
                for idx, (v, rev_idx) in enumerate(graph.graph[i]):
                    if v == n + j:
                        edge_idx = graph.get_edge_idx(i, idx)
                        break
                if edge_idx is not None:
                    result += graph.flow[edge_idx]
                    
    print(result)

if __name__ == "__main__":
    main()
