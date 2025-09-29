
def main():
    with open("INPUT.TXT", "r") as f:
        data = f.read().strip()
    
    parts = data.split()
    n = int(parts[0])
    k = len(parts[1])
    
    result = 1
    current = n
    
    while current > 0:
        result *= current
        current -= k
        if current <= 0:
            break
    
    print(result)

if __name__ == "__main__":
    main()
