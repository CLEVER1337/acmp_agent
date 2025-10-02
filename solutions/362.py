
with open('INPUT.TXT', 'r') as f:
    a, b = map(int, f.readline().split())
    c, d = map(int, f.readline().split())

if (a <= c and b <= d) or (a <= d and b <= c) or \
   (b <= c and a <= d) or (b <= d and a <= c):
    result = "Possible"
else:
    result = "Impossible"

with open('OUTPUT.TXT', 'w') as f:
    f.write(result)
