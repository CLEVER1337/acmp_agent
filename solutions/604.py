
MOD = 10**9 + 7

def main():
    import sys
    sys.setrecursionlimit(10000)
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    graph = [[] for _ in range(n+1)]
    index = 1
    for _ in range(n-1):
        u = int(data[index]); v = int(data[index+1]); index += 2
        graph[u].append(v)
        graph[v].append(u)
    
    parent = [0] * (n+1)
    children = [[] for _ in range(n+1)]
    order = []
    stack = [1]
    parent[1] = 0
    while stack:
        u = stack.pop()
        order.append(u)
        for v in graph[u]:
            if v == parent[u]:
                continue
            parent[v] = u
            children[u].append(v)
            stack.append(v)
    
    order.reverse()
    
    dp = [0] * (n+1)
    ways = [0] * (n+1)
    
    for u in order:
        dp[u] = 1
        ways[u] = 1
        
        for v in children[u]:
            dp[u] = (dp[u] * (dp[v] + 1)) % MOD
            
        k = len(children[u])
        if k == 0:
            continue
            
        pre = [1] * (k+1)
        suf = [1] * (k+1)
        
        for i in range(k):
            v = children[u][i]
            pre[i+1] = pre[i] * (dp[v] + 1) % MOD
            
        for i in range(k-1, -1, -1):
            v = children[u][i]
            suf[i] = suf[i+1] * (dp[v] + 1) % MOD
            
        for i in range(k):
            v = children[u][i]
            ways[u] = (ways[u] + ways[v] * pre[i] % MOD * suf[i+1] % MOD) % MOD
            
    print(ways[1] % MOD)

if __name__ == '__main__':
    main()
