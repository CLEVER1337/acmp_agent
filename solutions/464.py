
def main():
    with open("INPUT.TXT", "r") as f:
        n = int(f.read().strip())
    
    if n == 1:
        result = 0
    else:
        length = 1
        k = 0
        while length < n:
            k += 1
            length = length * 2 + 1
        
        pos = n - length // 2 - 1
        if k == 0:
            result = 0
        else:
            result = (k % 3 + pos) % 3
    
    with open("OUTPUT.TXT", "w") as f:
        f.write(str(result))

if __name__ == "__main__":
    main()
