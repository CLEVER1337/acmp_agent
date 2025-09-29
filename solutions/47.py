
def digit_sum(x):
    s = 0
    while x > 0:
        s += x % 10
        x //= 10
    return s

n = int(input())
best_divisor = 1

for i in range(1, n + 1):
    if n % i == 0:
        current_sum = digit_sum(i)
        best_sum = digit_sum(best_divisor)
        
        if current_sum > best_sum:
            best_divisor = i
        elif current_sum == best_sum:
            if i < best_divisor:
                best_divisor = i

print(best_divisor)
