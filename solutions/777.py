
with open('INPUT.TXT', 'r') as f:
    S, T = map(int, f.readline().split())

if T > S:
    result = T - S
else:
    result = 12 - S + T

print(result, file=open('OUTPUT.TXT', 'w'))
