
with open('INPUT.TXT', 'r') as f:
    N, M = map(int, f.readline().split())

base = N // M
remainder = N % M

result = []
for i in range(M):
    if i < M - remainder:
        result.append(base)
    else:
        result.append(base + 1)

with open('OUTPUT.TXT', 'w') as f:
    f.write(' '.join(map(str, result)))
