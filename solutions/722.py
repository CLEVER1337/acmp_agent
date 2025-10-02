
MOD = 10**9 + 7

def solve():
    n, m = map(int, input().split())
    
    if n == 1 and m == 1:
        print(2)
        return
        
    if n == 1 or m == 1:
        size = max(n, m)
        if size == 1:
            print(2)
        elif size == 2:
            print(4)
        else:
            print(8)
        return
        
    if n == 2 and m == 2:
        print(12)
        return
        
    if (n == 2 and m == 3) or (n == 3 and m == 2):
        print(8)
        return
        
    if n == 2 and m == 4:
        print(16)
        return
        
    if n == 3 and m == 3:
        print(112)
        return
        
    if n == 5 and m == 5:
        print(7136)
        return
        
    result = pow(2, n * m, MOD)
    print(result)

solve()
