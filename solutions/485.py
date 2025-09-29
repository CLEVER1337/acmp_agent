
def main():
    with open("INPUT.TXT", "r") as f:
        N, K = map(int, f.readline().split())
    
    x = 1
    while True:
        total = x
        valid = True
        for i in range(N):
            if (total - K) % N != 0:
                valid = False
                break
            total = (total - K) * (N - 1) // N
        if valid and total >= 0:
            break
        x += 1
    
    with open("OUTPUT.TXT", "w") as f:
        f.write(str(x))

if __name__ == "__main__":
    main()
