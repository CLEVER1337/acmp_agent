
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    numbers = list(map(int, data[1:1+n]))
    
    if n == 2:
        print(1)
        return
        
    for k in range(1, n):
        if n % k != 0:
            continue
            
        valid = True
        for i in range(k, n):
            if numbers[i] != numbers[i % k]:
                valid = False
                break
                
        if valid:
            print(k)
            return
            
    print(n - 1)

if __name__ == "__main__":
    main()
