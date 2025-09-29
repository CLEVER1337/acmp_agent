
def count_divisors(n):
    if n == 1:
        return 1
        
    count = 1
    i = 2
    while i * i <= n:
        if n % i == 0:
            exponent = 0
            while n % i == 0:
                exponent += 1
                n //= i
            count *= (exponent + 1)
        i += 1
        
    if n > 1:
        count *= 2
        
    return count

with open('INPUT.TXT', 'r') as f:
    x = int(f.read().strip())
    
result = count_divisors(x)

with open('OUTPUT.TXT', 'w') as f:
    f.write(str(result))
