
with open('INPUT.TXT', 'r') as f:
    N = int(f.read().strip())

total = 0
for i in range(N + 1):
    for j in range(i, N + 1):
        total += i + j

with open('OUTPUT.TXT', 'w') as f:
    f.write(str(total))
