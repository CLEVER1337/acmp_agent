
def solve():
    n = int(input().strip())
    if n < 3:
        return 0
    if n == 3:
        return 1
    
    def count_ways(n):
        if n <= 3:
            return 1
        if n % 2 == 0:
            return 2 * count_ways(n // 2)
        else:
            return count_ways(n // 2) + count_ways(n // 2 + 1)
    
    return count_ways(n)

print(solve())
