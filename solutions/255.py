
def main():
    with open("INPUT.TXT", "r") as f:
        N = int(f.readline().strip())
    
    if N % 2 == 0:
        A = N // 2
        B = N // 2
    else:
        for d in range(3, int(N**0.5) + 1, 2):
            if N % d == 0:
                A = d
                B = N - d
                break
        else:
            A = 1
            B = N - 1
    
    with open("OUTPUT.TXT", "w") as f:
        f.write(f"{A} {B}")

if __name__ == "__main__":
    main()
