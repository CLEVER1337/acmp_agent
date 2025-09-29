
with open('INPUT.TXT', 'r') as f:
    s = f.readline().strip()

current = 0
visited = {0}
min_floor = 0
max_floor = 0

for char in s:
    if char == '1':
        current += 1
    else:
        current -= 1
    visited.add(current)
    min_floor = min(min_floor, current)
    max_floor = max(max_floor, current)

result = max_floor - min_floor + 1
with open('OUTPUT.TXT', 'w') as f:
    f.write(str(result))
