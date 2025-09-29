
def convert(n):
    digits = []
    base = 3
    while n > 0:
        remainder = n % base
        if remainder == 0:
            digits.append('3')
            n = n // base - 1
        else:
            digits.append(str(remainder))
            n = n // base
    return ''.join(digits[::-1])

with open('INPUT.TXT', 'r') as f:
    n = int(f.read().strip())

result = convert(n)

with open('OUTPUT.TXT', 'w') as f:
    f.write(result)
