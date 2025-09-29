
with open('INPUT.TXT', 'r') as f:
    data = f.read().split()
    N = data[0]
    K = int(data[1])

result = 0
for digit in N:
    result = (result * 10 + int(digit)) % K

with open('OUTPUT.TXT', 'w') as f:
    f.write(str(result))
