
def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        print("No")
        return
        
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
        
    queue = []
    for i in range(1, n+1):
        if in_degree[i] == 0:
            queue.append(i)
            
    count = 0
    while queue:
        if len(queue) > 1:
            print("No")
            return
            
        u = queue.pop(0)
        count += 1
        
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
                
    if count == n:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
