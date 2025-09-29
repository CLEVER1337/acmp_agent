
n, m = map(int, input().split())
adj = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    adj[u-1].append(v-1)
    adj[v-1].append(u-1)

count = 0
for a in range(n):
    for b in adj[a]:
        if b <= a:
            continue
        for c in adj[b]:
            if c == a or c <= b:
                continue
            if a in adj[c]:
                count += 1

print(count)
