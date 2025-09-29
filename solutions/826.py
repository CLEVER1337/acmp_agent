
import sys
sys.setrecursionlimit(100000)

def main():
    data = sys.stdin.read().splitlines()
    if not data:
        print(-1)
        return
        
    n = int(data[0])
    graph = [[] for _ in range(n+1)]
    
    for i in range(1, n):
        u, v = map(int, data[i].split())
        graph[u].append(v)
        graph[v].append(u)
    
    constraints = [""] * (n+1)
    for i in range(n):
        constraints[i+1] = data[n-1+i+1].strip()
    
    if any(len(constraints[i]) == 0 for i in range(1, n+1)):
        print(-1)
        return
    
    dp = [[0]*3 for _ in range(n+1)]
    possible = [False] * (n+1)
    
    def dfs(u, parent):
        colors = []
        for char in constraints[u]:
            if char == 'I':
                colors.append(0)
            elif char == 'B':
                colors.append(1)
            elif char == 'V':
                colors.append(2)
        
        if not colors:
            possible[u] = False
            return
        
        for color in colors:
            dp[u][color] = 1 if color == 0 else 0
        
        for v in graph[u]:
            if v == parent:
                continue
            dfs(v, u)
            if not possible[v]:
                possible[u] = False
                return
                
            for u_color in range(3):
                if dp[u][u_color] == -1:
                    continue
                    
                best = -1
                for v_color in range(3):
                    if u_color != v_color and dp[v][v_color] != -1:
                        total = dp[u][u_color] + dp[v][v_color]
                        if total > best:
                            best = total
                
                if best == -1:
                    dp[u][u_color] = -1
                else:
                    dp[u][u_color] = best
        
        possible[u] = any(dp[u][color] != -1 for color in range(3))
    
    root = 1
    dfs(root, -1)
    
    if not possible[root]:
        print(-1)
    else:
        result = max(dp[root])
        print(result)

if __name__ == "__main__":
    main()
