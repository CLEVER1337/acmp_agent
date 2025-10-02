
def main():
    with open("INPUT.TXT", "r") as f:
        data = f.read().split()
        n = int(data[0])
        m = int(data[1])
    
    if n > m:
        n, m = m, n
        
    if n == 0:
        result = m * (m + 1) // 2
    else:
        k = 0
        while (1 << k) <= n:
            k += 1
        
        result = ((n + 1) * (m + 1) - (1 << (2 * k))) // 3 + (1 << (2 * k - 1))
    
    with open("OUTPUT.TXT", "w") as f:
        f.write(str(result))

if __name__ == "__main__":
    main()
