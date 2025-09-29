
k = int(input())
groups = list(map(int, input().split()))

groups.sort()

half_groups = k // 2 + 1
min_supporters = 0

for i in range(half_groups):
    min_supporters += groups[i] // 2 + 1

print(min_supporters)
