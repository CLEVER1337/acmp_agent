
with open('INPUT.TXT', 'r') as f:
    a, b, c = map(int, f.read().split())

result = []

if a != 0:
    result.append(str(a))

if b != 0:
    if b == 1:
        result.append('x')
    elif b == -1:
        result.append('-x')
    else:
        result.append(f"{b}x")

if c != 0:
    if c == 1:
        result.append('+y')
    elif c == -1:
        result.append('-y')
    else:
        if c > 0 and result:
            result.append(f"+{c}y")
        else:
            result.append(f"{c}y")

if not result:
    result.append('0')

with open('OUTPUT.TXT', 'w') as f:
    f.write(''.join(result))
