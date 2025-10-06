
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    p_list = list(map(int, data[1:1+n]))
    index = 1 + n
    
    graph = [[] for _ in range(n+1)]
    in_degree = [0] * (n+1)
    required_parts = [0] * (n+1)
    
    for i in range(1, n+1):
        k = int(data[index]); index += 1
        required_parts[i] = k
        for j in range(k):
            part = int(data[index]); index += 1
            graph[part].append(i)
            in_degree[i] += 1
    
    time_needed = [0] * (n+1)
    order = []
    q = deque()
    
    for i in range(1, n+1):
        if in_degree[i] == 0:
            q.append(i)
            time_needed[i] = p_list[i-1]
    
    while q:
        u = q.popleft()
        order.append(u)
        for v in graph[u]:
            if time_needed[v] < time_needed[u] + p_list[v-1]:
                time_needed[v] = time_needed[u] + p_list[v-1]
            in_degree[v] -= 1
            if in_degree[v] == 0:
                q.append(v)
    
    target_time = time_needed[1]
    result_order = []
    visited = [False] * (n+1)
    q2 = deque([1])
    visited[1] = True
    
    while q2:
        u = q2.popleft()
        result_order.append(u)
        if required_parts[u] > 0:
            dependencies = []
            for i in range(1, n+1):
                if u in graph[i] and required_parts[i] > 0:
                    dependencies.append((time_needed[i], i))
            dependencies.sort(reverse=True)
            for _, dep in dependencies:
                if not visited[dep]:
                    visited[dep] = True
                    q2.append(dep)
    
    result_order.reverse()
    k = len(result_order)
    print(f"{target_time} {k}")
    print(" ".join(map(str, result_order)))

if __name__ == "__main__":
    main()
