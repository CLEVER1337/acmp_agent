
with open('INPUT.TXT', 'r') as f:
    n = int(f.read().strip())

result = n * (n - 1) * (n - 2)

with open('OUTPUT.TXT', 'w') as f:
    f.write(str(result))
