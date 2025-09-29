
s = input().strip()
if s[1] == '+':
    if s[0] == 'x':
        result = int(s[4]) - int(s[2])
    elif s[2] == 'x':
        result = int(s[4]) - int(s[0])
    else:
        result = int(s[0]) + int(s[2])
else:
    if s[0] == 'x':
        result = int(s[4]) + int(s[2])
    elif s[2] == 'x':
        result = int(s[0]) - int(s[4])
    else:
        result = int(s[0]) - int(s[2])
print(result)
