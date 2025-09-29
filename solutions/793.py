
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def digit_sum(n):
    return sum(int(d) for d in str(n))

def is_smith(n):
    if is_prime(n):
        return False
        
    original_sum = digit_sum(n)
    prime_factors_sum = 0
    temp = n
    
    divisor = 2
    while temp > 1:
        if temp % divisor == 0 and is_prime(divisor):
            while temp % divisor == 0:
                prime_factors_sum += digit_sum(divisor)
                temp //= divisor
        divisor += 1
        
    return original_sum == prime_factors_sum

with open('INPUT.TXT', 'r') as f:
    numbers = list(map(int, f.read().split()))
    
result = ''.join('1' if is_smith(n) else '0' for n in numbers)

with open('OUTPUT.TXT', 'w') as f:
    f.write(result)
