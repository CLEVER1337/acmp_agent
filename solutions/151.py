
def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        print("YES")
        return
        
    n = int(data[0])
    m = int(data[1])
    
    if n == 0:
        print("YES")
        return
        
    graph = [[] for _ in range(n + 1)]
    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        index += 2
        graph[u].append(v)
        graph[v].append(u)
    
    color = [-1] * (n + 1)
    
    for i in range(1, n + 1):
        if color[i] == -1:
            stack = [i]
            color[i] = 0
            while stack:
                node = stack.pop()
                for neighbor in graph[node]:
                    if color[neighbor] == -1:
                        color[neighbor] = color[node] ^ 1
                        stack.append(neighbor)
                    elif color[neighbor] == color[node]:
                        print("NO")
                        return
    print("YES")

if __name__ == "__main__":
    main()
