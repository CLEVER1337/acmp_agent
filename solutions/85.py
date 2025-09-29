
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

n, m = map(int, input().split())
result = gcd(n, m)
print('1' * result)
