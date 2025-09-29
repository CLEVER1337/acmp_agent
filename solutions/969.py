
def main():
    with open("INPUT.TXT", "r") as f:
        n, m = map(int, f.read().split())
    
    if n == 0:
        result = 1 % m
    elif n == 1:
        result = 2 % m
    else:
        def tetration_mod(n, m):
            if n == 1:
                return 2 % m
                
            def euler_phi(k):
                result = k
                i = 2
                while i * i <= k:
                    if k % i == 0:
                        while k % i == 0:
                            k //= i
                        result -= result // i
                    i += 1
                if k > 1:
                    result -= result // k
                return result
                
            def power_mod(base, exp, mod):
                result = 1
                base %= mod
                while exp:
                    if exp & 1:
                        result = (result * base) % mod
                    base = (base * base) % mod
                    exp >>= 1
                return result
                
            def hyper_power(n, mod):
                if mod == 1:
                    return 0
                if n == 1:
                    return 2 % mod
                    
                phi = euler_phi(mod)
                exponent = hyper_power(n - 1, phi)
                return power_mod(2, exponent + phi, mod)
                
            result = hyper_power(n, m)
        
    with open("OUTPUT.TXT", "w") as f:
        f.write(str(result))

if __name__ == "__main__":
    main()
