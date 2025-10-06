
s = input().strip()
a = 0
ab = 0
abc = 0
for char in s:
    if char == 'a':
        a += 1
    elif char == 'b':
        ab += a
    elif char == 'c':
        abc += ab
print(abc)
