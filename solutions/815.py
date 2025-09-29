
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0]); m = int(data[1]); k = int(data[2])
    index = 3
    
    graph = [[] for _ in range(n+1)]
    for i in range(m):
        u = int(data[index]); v = int(data[index+1]); c = int(data[index+2])
        index += 3
        graph[u].append((v, c))
    
    L = int(data[index]); index += 1
    program = list(map(int, data[index:index+L]))
    index += L
    s = int(data[index])
    
    dp = [[False] * (L+1) for _ in range(n+1)]
    dp[s][0] = True
    
    for step in range(L):
        color = program[step]
        for u in range(1, n+1):
            if not dp[u][step]:
                continue
            for (v, c) in graph[u]:
                if c == color:
                    dp[v][step+1] = True
    
    final_states = []
    for i in range(1, n+1):
        if dp[i][L]:
            final_states.append(i)
            
    if not final_states:
        print("Hangs")
    else:
        print("OK")
        print(len(final_states))
        final_states.sort()
        print(" ".join(map(str, final_states)))

if __name__ == "__main__":
    main()
