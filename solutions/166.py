
k, n = map(int, input().split())
robots = [k]
for year in range(2, n + 1):
    new_robots = sum(robots[:-1]) if len(robots) > 1 else 0
    robots.append(new_robots)
    if len(robots) > 3:
        robots.pop(0)
print(sum(robots))
