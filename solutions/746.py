
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
        common = 0
        for neighbor in adj[a]:
            if neighbor in adj[b]:
                common += 1
        count += common * (common - 1) // 2

print(count)
