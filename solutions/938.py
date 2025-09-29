
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_prime_divisors(x):
    count = 0
    for i in range(2, x + 1):
        if x % i == 0 and is_prime(i):
            count += 1
    return count

with open('INPUT.TXT', 'r') as f:
    n = int(f.readline().strip())
    numbers = list(map(int, f.readline().split()))

max_divisors = -1
result = float('inf')

for num in numbers:
    divisors_count = count_prime_divisors(num)
    if divisors_count > max_divisors:
        max_divisors = divisors_count
        result = num
    elif divisors_count == max_divisors and num < result:
        result = num

with open('OUTPUT.TXT', 'w') as f:
    f.write(str(result))
