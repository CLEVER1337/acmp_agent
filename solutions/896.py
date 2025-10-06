
def main():
    import sys
    data = sys.stdin.read().split()
    M = int(data[0])
    N = int(data[1])
    
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    g = gcd(M, N)
    lcm = M * N // g
    result = lcm // M + lcm // N - (1 if lcm == M or lcm == N else 2)
    print(result)

if __name__ == "__main__":
    main()
