
def solve():
    n = int(input().strip())
    if n < 3:
        return 0
    if n == 3:
        return 1
    
    ways = 1
    while n > 3:
        if n % 2 == 0:
            ways *= 2
            n //= 2
        else:
            ways *= 2
            n = (n + 1) // 2
    return ways

print(solve())
