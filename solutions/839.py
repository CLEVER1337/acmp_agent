
with open('INPUT.TXT', 'r') as f:
    data = f.read().strip()

if '0' in data:
    print('NO')
else:
    print('YES')
