
with open('INPUT.TXT', 'r') as f:
    s = f.read().strip()

result = []
i = 0
n = len(s)

while i < n:
    if s[i] == '1':
        result.append('a')
        i += 1
    else:
        count_zeros = 0
        while i < n and s[i] == '0':
            count_zeros += 1
            i += 1
        if i < n and s[i] == '1':
            result.append(chr(ord('a') + count_zeros))
            i += 1

with open('OUTPUT.TXT', 'w') as f:
    f.write(''.join(result))
