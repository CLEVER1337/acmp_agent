
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def main():
    with open('INPUT.TXT', 'r') as f:
        M, N = map(int, f.read().split())
    
    if M == N:
        result = M
    else:
        g = gcd(M, N)
        l = lcm(M, N)
        result = l // g + M + N - g - (l // M) - (l // N)
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(result))

if __name__ == '__main__':
    main()
