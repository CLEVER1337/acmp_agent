
def main():
    with open("INPUT.TXT", "r") as f:
        data = f.read().split()
        N = int(data[0])
        M = int(data[1])
    
    remainder = N % M
    if remainder == 0:
        K = 0
    else:
        K = M - remainder
    
    with open("OUTPUT.TXT", "w") as f:
        f.write(str(K))

if __name__ == "__main__":
    main()
