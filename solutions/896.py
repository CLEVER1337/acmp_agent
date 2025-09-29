
def main():
    with open("INPUT.TXT", "r") as f:
        M, N = map(int, f.readline().split())
    
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    lcm = M * N // gcd(M, N)
    result = lcm // M + lcm // N - gcd(M, N)
    
    with open("OUTPUT.TXT", "w") as f:
        f.write(str(result))

if __name__ == "__main__":
    main()
