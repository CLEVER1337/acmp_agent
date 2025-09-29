
n = int(input())
s = input().strip()

if n == 0:
    print('0')
    exit()

if all(c == '0' for c in s):
    print('0')
    exit()

result = []
for i in range(n):
    if s[i] == '1':
        result.append('1')
    else:
        break

if len(result) < n:
    result.append('0')

print(''.join(result))
