
n, m = map(int, input().split())
adj = [[0] * n for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    adj[u][v] = 1
    adj[v][u] = 1

count = 0
for a in range(n):
    for b in range(n):
        if a == b or not adj[a][b]:
            continue
        for c in range(n):
            if c == a or c == b or not adj[b][c]:
                continue
            for d in range(n):
                if d == a or d == b or d == c or not adj[c][d]:
                    continue
                if adj[d][a]:
                    count += 1

print(count // 8)
