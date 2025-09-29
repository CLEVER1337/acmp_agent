
s = input().strip()
n = int(input())
messages = [input().strip() for _ in range(n)]

min_hamming = float('inf')
results = []

for i, m in enumerate(messages, 1):
    hamming = sum(1 for a, b in zip(s, m) if a != b)
    if hamming < min_hamming:
        min_hamming = hamming
        results = [i]
    elif hamming == min_hamming:
        results.append(i)

print(len(results))
print(' '.join(map(str, sorted(results))))
