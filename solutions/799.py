
n = int(input().strip())
scores = list(map(int, input().split()))

max_score = max(scores)
candidates = []

for i in range(n):
    if scores[i] % 10 == 5:
        if i < n - 1 and scores[i] > scores[i + 1]:
            candidates.append(scores[i])

if not candidates:
    print(0)
else:
    best_candidate = max(candidates)
    count_better = 0
    for score in scores:
        if score > best_candidate:
            count_better += 1
    place = count_better + 1
    print(place)
