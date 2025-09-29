
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    p = list(map(int, data[1:1+n]))
    
    index = 1 + n
    graph = [[] for _ in range(n+1)]
    in_degree = [0] * (n+1)
    dependencies = [[] for _ in range(n+1)]
    
    for i in range(1, n+1):
        k = int(data[index]); index += 1
        in_degree[i] = k
        for j in range(k):
            dep = int(data[index]); index += 1
            graph[dep].append(i)
            dependencies[i].append(dep)
    
    # Topological sort with Kahn's algorithm
    q = deque()
    for i in range(1, n+1):
        if in_degree[i] == 0:
            q.append(i)
    
    topo_order = []
    while q:
        u = q.popleft()
        topo_order.append(u)
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                q.append(v)
    
    # DP for minimum time to produce each part
    dp = [0] * (n+1)
    for node in topo_order:
        max_dep_time = 0
        for dep in dependencies[node]:
            max_dep_time = max(max_dep_time, dp[dep])
        dp[node] = max_dep_time + p[node-1]
    
    # Find all parts needed for part 1
    needed_parts = set()
    stack = [1]
    while stack:
        current = stack.pop()
        if current not in needed_parts:
            needed_parts.add(current)
            for dep in dependencies[current]:
                stack.append(dep)
    
    # Get topological order of only needed parts
    needed_topo = [node for node in topo_order if node in needed_parts]
    
    print(f"{dp[1]} {len(needed_topo)}")
    print(" ".join(map(str, needed_topo)))

if __name__ == "__main__":
    main()
