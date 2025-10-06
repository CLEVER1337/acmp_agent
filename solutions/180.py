
def main():
    import sys
    data = sys.stdin.read().split()
    N = int(data[0])
    K = int(data[1])
    
    if K == 0:
        print("YES")
        return
        
    def digit_product(x):
        res = 1
        while x > 0:
            digit = x % 10
            if digit == 0:
                return 0
            res *= digit
            x //= 10
        return res

    def check():
        if K == 1:
            return True
            
        k_temp = K
        factors = []
        while k_temp > 1:
            found = False
            for d in range(9, 1, -1):
                if k_temp % d == 0:
                    factors.append(d)
                    k_temp //= d
                    found = True
                    break
            if not found:
                return False
                
        factors.sort()
        num = 0
        for d in factors:
            num = num * 10 + d
            if num > N:
                return False
                
        return num <= N and num > 0
        
    if check():
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
