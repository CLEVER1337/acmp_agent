
def convert_to_base(n, base):
    digits = []
    if n == 0:
        return '0'
    while n > 0:
        remainder = n % base
        if remainder < 10:
            digits.append(str(remainder))
        else:
            digits.append(chr(ord('A') + remainder - 10))
        n //= base
    return ''.join(reversed(digits))

with open('INPUT.TXT', 'r') as f:
    data = f.read().strip().split('/')
    D, M, Y = map(int, data)

base = D + 1
D_base = convert_to_base(D, base)
M_base = convert_to_base(M, base)
Y_base = convert_to_base(Y, base)

with open('OUTPUT.TXT', 'w') as f:
    f.write(f"{D_base}/{M_base}/{Y_base}")
