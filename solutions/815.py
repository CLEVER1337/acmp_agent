
from collections import deque

def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        return
    
    idx = 0
    n = int(data[idx]); m = int(data[idx+1]); k = int(data[idx+2]); idx += 3
    
    graph = [[] for _ in range(n+1)]
    for i in range(m):
        u = int(data[idx]); v = int(data[idx+1]); c = int(data[idx+2]); idx += 3
        graph[u].append((v, c))
    
    L = int(data[idx]); idx += 1
    program = list(map(int, data[idx:idx+L]))
    idx += L
    s = int(data[idx]); idx += 1
    
    dp = [[False] * (L+1) for _ in range(n+1)]
    dp[s][0] = True
    
    for step in range(L):
        color_needed = program[step]
        for u in range(1, n+1):
            if dp[u][step]:
                for (v, c) in graph[u]:
                    if c == color_needed:
                        dp[v][step+1] = True
    
    final_rooms = []
    for room in range(1, n+1):
        if dp[room][L]:
            final_rooms.append(room)
    
    if not final_rooms:
        print("Hangs")
    else:
        print("OK")
        print(len(final_rooms))
        print(" ".join(map(str, sorted(final_rooms))))

if __name__ == "__main__":
    main()
