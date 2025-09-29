
k, n, m, d = map(int, input().split())

def solve():
    for total in range(d + 1, 1000000):
        first = total // k
        second = total // n
        third = total // m
        rest = total - first - second - third
        
        if rest == d:
            return total
    return -1

print(solve())
