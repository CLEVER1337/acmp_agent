
def main():
    with open("INPUT.TXT", "r") as f:
        n, k = map(int, f.read().split())
    
    if k > n:
        result = 0
    else:
        result = 1
        for i in range(k):
            result = result * (n - i) * (n - i) // (i + 1)
    
    with open("OUTPUT.TXT", "w") as f:
        f.write(str(result))

if __name__ == "__main__":
    main()
