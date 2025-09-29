
def main():
    with open('INPUT.TXT', 'r') as f:
        data = f.read().split()
    
    n = int(data[0])
    m = int(data[1])
    
    graph = [[] for _ in range(n+1)]
    in_degree = [0] * (n+1)
    
    index = 2
    for i in range(m):
        a = int(data[index])
        b = int(data[index+1])
        index += 2
        graph[a].append(b)
        in_degree[b] += 1
    
    from collections import deque
    q = deque()
    
    for i in range(1, n+1):
        if in_degree[i] == 0:
            q.append(i)
    
    count = 0
    while q:
        if len(q) > 1:
            with open('OUTPUT.TXT', 'w') as f:
                f.write("No")
            return
        
        u = q.popleft()
        count += 1
        
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                q.append(v)
    
    if count == n:
        with open('OUTPUT.TXT', 'w') as f:
            f.write("Yes")
    else:
        with open('OUTPUT.TXT', 'w') as f:
            f.write("No")

if __name__ == "__main__":
    main()
