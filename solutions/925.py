
def main():
    with open("INPUT.TXT", "r") as f:
        mode = int(f.readline().strip())
        n, a, b, c = map(int, f.readline().split())
    
    if mode == 1:
        # Минимальное количество
        result = max(0, a + b + c - 2 * n)
    else:
        # Максимальное количество
        result = min(a, b, c)
    
    with open("OUTPUT.TXT", "w") as f:
        f.write(str(result))

if __name__ == "__main__":
    main()
