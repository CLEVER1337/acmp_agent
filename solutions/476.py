
def main():
    with open("INPUT.TXT", "r") as f:
        M, N = map(int, f.readline().split())
    
    if M == N:
        winner = 2 if (M - 1) % 2 == 1 else 1
    else:
        min_val = min(M, N)
        winner = 2 if min_val % 2 == 1 else 1
    
    with open("OUTPUT.TXT", "w") as f:
        f.write(str(winner))

if __name__ == "__main__":
    main()
