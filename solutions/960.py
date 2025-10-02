
s = input().strip()

a_count = 0
ab_count = 0
abc_count = 0

for char in s:
    if char == 'a':
        a_count += 1
    elif char == 'b':
        ab_count += a_count
    elif char == 'c':
        abc_count += ab_count

print(abc_count)
