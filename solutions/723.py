
def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    m = int(data[1])
    edges = []
    index = 2
    for i in range(m):
        a = int(data[index])
        b = int(data[index+1])
        t = int(data[index+2])
        index += 3
        edges.append((a, b, t))
    
    INF = 10**9
    dist = [-INF] * (n+1)
    dist[1] = 0
    
    for i in range(n-1):
        updated = False
        for a, b, t in edges:
            if dist[a] != -INF:
                if dist[b] < dist[a] + t:
                    dist[b] = dist[a] + t
                    updated = True
        if not updated:
            break
    
    in_cycle = [False] * (n+1)
    for i in range(n):
        updated = False
        for a, b, t in edges:
            if dist[a] != -INF:
                if dist[b] < dist[a] + t:
                    dist[b] = INF
                    in_cycle[b] = True
                    updated = True
        if not updated:
            break
    
    result = []
    for i in range(2, n+1):
        if dist[i] == INF or in_cycle[i]:
            result.append("-1")
        else:
            result.append(str(dist[i]))
    
    print(" ".join(result))

if __name__ == "__main__":
    main()
