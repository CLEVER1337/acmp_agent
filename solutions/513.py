
with open('INPUT.TXT', 'r') as f:
    n = int(f.read().strip())

result = (1 << n) - n - 1

with open('OUTPUT.TXT', 'w') as f:
    f.write(str(result))
