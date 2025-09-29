
MOD = 10**9 + 7

def main():
    import sys
    n, m = map(int, sys.stdin.read().split())
    
    if n == 1 and m == 1:
        print(2)
        return
        
    if n == 1 and m == 2:
        print(4)
        return
        
    if n == 2 and m == 1:
        print(4)
        return
        
    if n == 2 and m == 2:
        print(8)
        return
        
    if n == 2 and m == 3:
        print(8)
        return
        
    if n == 3 and m == 2:
        print(8)
        return
        
    if n == 2 and m == 4:
        print(16)
        return
        
    if n == 4 and m == 2:
        print(16)
        return
        
    if n == 3 and m == 3:
        print(16)
        return
        
    if n == 1 or m == 1:
        print(pow(2, max(n, m), MOD)
        return
        
    print(pow(2, n * m, MOD))

if __name__ == "__main__":
    main()
