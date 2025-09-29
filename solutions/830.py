
def main():
    with open("INPUT.TXT", "r") as f:
        n, m = map(int, f.readline().split())
    
    if n < m:
        n, m = m, n
        
    k = 0
    while (1 << (k + 1)) <= m:
        k += 1
        
    result = ((1 << (2 * k)) + 3 * (1 << k)) // 3
    result += (n + m - (1 << (k + 1)) + 1) * (1 << k)
    result += (n - m) * m
    
    with open("OUTPUT.TXT", "w") as f:
        f.write(str(result))

if __name__ == "__main__":
    main()
