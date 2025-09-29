
with open('INPUT.TXT', 'r') as f:
    sides = list(map(int, f.readline().split()))
    r = int(f.readline())

a, b, c = sorted(sides)

p = (a + b + c) / 2
s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
max_r = s / p

with open('OUTPUT.TXT', 'w') as f:
    f.write('YES' if r <= max_r else 'NO')
