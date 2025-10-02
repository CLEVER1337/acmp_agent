
import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

def get_direction(x, y):
    g = gcd(x, y)
    dx, dy = x // g, y // g
    if dx == 0:
        return (0, 1 if dy > 0 else -1)
    if dy == 0:
        return (1 if dx > 0 else -1, 0)
    return (dx, dy)

n = int(input())
targets = []

for _ in range(n):
    x, y = map(int, input().split())
    targets.append((x, y))

max_count = 0
directions = {}

for x, y in targets:
    direction = get_direction(x, y)
    directions[direction] = directions.get(direction, 0) + 1

max_count = max(directions.values()) if directions else 0

print(max_count)
