
k, n = map(int, input().split())
robots = [0] * (n + 1)
robots[1] = k

for year in range(2, n + 1):
    robots[year] = robots[year - 1] + robots[year - 2]

print(robots[n])
