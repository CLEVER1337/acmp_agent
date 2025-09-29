
n = int(input())
arr = list(map(int, input().split()))

from collections import Counter
counts = Counter(arr)
max_count = max(counts.values())
candidates = [num for num, cnt in counts.items() if cnt == max_count]
target_num = min(candidates)

result = [x for x in arr if x != target_num]
result.extend([target_num] * max_count)

print(' '.join(map(str, result)))
