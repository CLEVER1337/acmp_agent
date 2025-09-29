
with open('INPUT.TXT', 'r') as f:
    n = int(f.readline().strip())
    times = []
    for _ in range(n):
        h, m, s = map(int, f.readline().split())
        times.append((h, m, s))

times.sort(key=lambda x: (x[0], x[1], x[2]))

with open('OUTPUT.TXT', 'w') as f:
    for h, m, s in times:
        f.write(f"{h} {m} {s}\n")
