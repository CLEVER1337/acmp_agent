
def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    
    if n == 0:
        result = 1 % m
    else:
        def phi(x):
            res = x
            i = 2
            while i * i <= x:
                if x % i == 0:
                    while x % i == 0:
                        x //= i
                    res -= res // i
                i += 1
            if x > 1:
                res -= res // x
            return res
        
        def power_mod(a, b, mod):
            result = 1
            a = a % mod
            while b > 0:
                if b % 2 == 1:
                    result = (result * a) % mod
                a = (a * a) % mod
                b //= 2
            return result
        
        def tetration_mod(n, mod):
            if mod == 1:
                return 0
            if n == 0:
                return 1 % mod
            if n == 1:
                return 2 % mod
            if n == 2:
                return 4 % mod
            if n == 3:
                return 16 % mod
            
            phi_mod = phi(mod)
            exp = tetration_mod(n - 1, phi_mod)
            if exp == 0:
                exp = phi_mod
            return power_mod(2, exp, mod)
        
        result = tetration_mod(n, m)
    
    print(result)

if __name__ == "__main__":
    main()
