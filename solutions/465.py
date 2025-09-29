
def main():
    with open("INPUT.TXT", "r") as f:
        n = int(f.read().strip())
    
    if n == 1:
        result = 2
    else:
        a, b = 2, 3
        for i in range(3, n + 1):
            a, b = b, a + b
        result = b
    
    with open("OUTPUT.TXT", "w") as f:
        f.write(str(result))

if __name__ == "__main__":
    main()
