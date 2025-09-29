
def main():
    import sys
    n, m, k = map(int, sys.stdin.readline().split())
    
    if k == 1:
        print(n * m)
        return
        
    def calc_max(x):
        a = x % k
        b = x // k
        return a + b
        
    max_needed = 0
    for x in range(1, m + 1):
        current = calc_max(x)
        if current > max_needed:
            max_needed = current
            
    print(n * max_needed)

if __name__ == "__main__":
    main()
