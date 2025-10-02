
def fib_to_dec(s):
    fibs = [1, 2]
    while len(fibs) < len(s):
        fibs.append(fibs[-1] + fibs[-2])
    fibs.reverse()
    total = 0
    for i, char in enumerate(s):
        if char == '1':
            total += fibs[i]
    return total

def dec_to_fib(n):
    if n == 0:
        return '0'
    
    fibs = [1, 2]
    while fibs[-1] <= n:
        fibs.append(fibs[-1] + fibs[-2])
    fibs.pop()
    fibs.reverse()
    
    result = []
    for fib in fibs:
        if n >= fib:
            result.append('1')
            n -= fib
        else:
            result.append('0')
    
    return ''.join(result).lstrip('0')

def normalize_fib(s):
    n = fib_to_dec(s)
    return dec_to_fib(n)

def add_fib_numbers(a, b):
    num_a = fib_to_dec(a)
    num_b = fib_to_dec(b)
    total = num_a + num_b
    return dec_to_fib(total)

with open('INPUT.TXT', 'r') as f:
    a_str = f.readline().strip()
    b_str = f.readline().strip()

result = add_fib_numbers(a_str, b_str)

with open('OUTPUT.TXT', 'w') as f:
    f.write(result)
