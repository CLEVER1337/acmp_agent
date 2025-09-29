
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def digit_sum(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s

a, b = map(int, open('INPUT.TXT').read().split())
max_sum = -1
max_prime = -1

for num in range(a, b + 1):
    if is_prime(num):
        s = digit_sum(num)
        if s > max_sum:
            max_sum = s
            max_prime = num
        elif s == max_sum:
            if num > max_prime:
                max_prime = num

open('OUTPUT.TXT', 'w').write(str(max_prime))
