
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    graph = [[] for _ in range(n+1)]
    in_degree = [0] * (n+1)
    dependencies = [0] * (n+1)
    required = [0] * (n+1)
    index = 1
    
    for i in range(1, n+1):
        nums = []
        while index < len(data) and data[index] != '0':
            num = int(data[index])
            nums.append(num)
            index += 1
        index += 1
        
        dependencies[i] = len(nums)
        required[i] = (dependencies[i] + 1) // 2
        for dep in nums:
            graph[dep].append(i)
            in_degree[i] += 1
    
    q = deque()
    for i in range(1, n+1):
        if in_degree[i] == 0:
            q.append(i)
    
    order = []
    proved = [False] * (n+1)
    count_deps = [0] * (n+1)
    
    while q:
        u = q.popleft()
        order.append(u)
        proved[u] = True
        
        for v in graph[u]:
            count_deps[v] += 1
            if count_deps[v] >= required[v] and not proved[v]:
                proved[v] = True
                q.append(v)
    
    main_theorem_path = []
    visited = [False] * (n+1)
    
    def dfs(node):
        if visited[node]:
            return
        visited[node] = True
        main_theorem_path.append(node)
        if node == 1:
            return
        for dep in graph[node]:
            if proved[dep] and not visited[dep]:
                dfs(dep)
    
    dfs(1)
    main_theorem_path.reverse()
    
    result_set = set()
    result_order = []
    
    for node in main_theorem_path:
        result_set.add(node)
        result_order.append(node)
    
    for node in order:
        if node not in result_set:
            result_order.append(node)
    
    print(len(result_order))
    for node in result_order:
        print(node)

if __name__ == "__main__":
    main()
