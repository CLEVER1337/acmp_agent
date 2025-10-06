
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    it = iter(data)
    n = int(next(it)); m = int(next(it)); k = int(next(it))
    
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        u = int(next(it)); v = int(next(it)); c = int(next(it))
        graph[u].append((v, c))
    
    L = int(next(it))
    program = [int(next(it)) for _ in range(L)]
    s = int(next(it))
    
    dp = [[False] * (n+1) for _ in range(L+1)]
    dp[0][s] = True
    
    for step in range(L):
        color_needed = program[step]
        for room in range(1, n+1):
            if dp[step][room]:
                for neighbor, color in graph[room]:
                    if color == color_needed:
                        dp[step+1][neighbor] = True
    
    if not any(dp[L]):
        print("Hangs")
        return
    
    reachable = [i for i in range(1, n+1) if dp[L][i]]
    reachable.sort()
    print("OK")
    print(len(reachable))
    print(" ".join(map(str, reachable)))

if __name__ == "__main__":
    main()
