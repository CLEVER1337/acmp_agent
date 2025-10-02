
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
        constraints[i+1] = data[n + i].strip()
    
    dp = [[-1] * 3 for _ in range(n+1)]
    
    def dfs(u, parent, color):
        if dp[u][color] != -1:
            return dp[u][color]
            
        allowed_colors = []
        if 'I' in constraints[u]:
            allowed_colors.append(0)
        if 'B' in constraints[u]:
            allowed_colors.append(1)
        if 'V' in constraints[u]:
            allowed_colors.append(2)
            
        if color not in allowed_colors:
            dp[u][color] = -10**9
            return -10**9
            
        total = 1 if color == 0 else 0
        for v in graph[u]:
            if v == parent:
                continue
                
            best = -10**9
            for next_color in range(3):
                if next_color != color:
                    res = dfs(v, u, next_color)
                    if res > best:
                        best = res
                        
            if best == -10**9:
                dp[u][color] = -10**9
                return -10**9
                
            total += best
            
        dp[u][color] = total
        return total
        
    result = -1
    for color in range(3):
        res = dfs(1, -1, color)
        if res > result:
            result = res
            
    if result < 0:
        print(-1)
    else:
        print(result)

if __name__ == "__main__":
    main()
