
def main():
    with open("INPUT.TXT", "r") as f:
        n = int(f.read().strip())
    
    if n <= 2:
        print(1)
        return
        
    result = 0
    for k in range(1, n):
        term = (n * (n - 1)) // 2
        result += (k ** (n - 2)) * (term ** k)
    
    with open("OUTPUT.TXT", "w") as f:
        f.write(str(result))

if __name__ == "__main__":
    main()
