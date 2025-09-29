
def main():
    with open("INPUT.TXT", "r") as f:
        N, M = map(int, f.read().split())
    
    remainder = N % M
    if remainder == 0:
        K = 0
    else:
        K = M - remainder
    
    with open("OUTPUT.TXT", "w") as f:
        f.write(str(K))

if __name__ == "__main__":
    main()
