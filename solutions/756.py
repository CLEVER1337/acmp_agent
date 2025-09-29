
def main():
    with open("INPUT.TXT", "r") as f:
        M, N = map(int, f.readline().split())
    
    result = M * (N - 1) + (M - 1) * N - (M * N - 1)
    
    with open("OUTPUT.TXT", "w") as f:
        f.write(str(result))

if __name__ == "__main__":
    main()
