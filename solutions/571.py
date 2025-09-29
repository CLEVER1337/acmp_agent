
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    directions = list(map(int, data[1:1+n]))
    
    if n < 3:
        print(0)
        return
        
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i+1] = prefix[i] + (1 if directions[i] % 2 == 1 else -1)
        
    total = 0
    for i in range(n):
        for j in range(i+2, n+1):
            if j - i > n - 2:
                continue
            if prefix[i] == prefix[j] and (j - i) % 3 == 0:
                k = (j - i) // 3
                if prefix[i+k] == prefix[i] + k and prefix[i+2*k] == prefix[i] + 2*k:
                    total += 1
                    
    print(total)

if __name__ == "__main__":
    main()
