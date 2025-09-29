
with open('INPUT.TXT', 'r') as f:
    k = int(f.readline().strip())
    results = []
    for _ in range(k):
        a, b = f.readline().split()
        set_a = set(str(a))
        set_b = set(str(b))
        results.append('YES' if set_a == set_b else 'NO')

with open('OUTPUT.TXT', 'w') as f:
    for result in results:
        f.write(result + '\n')
