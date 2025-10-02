
def main():
    with open('input.txt', 'r') as f:
        n, m = map(int, f.read().split())
    
    if n == 0:
        result = 1 % m
    elif n == 1:
        result = 2 % m
    else:
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
        
        def power_mod(a, b, mod):
            if mod == 1:
                return 0
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
            
            phi = euler_phi(mod)
            exp = tetration_mod(n - 1, phi)
            return power_mod(2, exp + phi, mod)
        
        result = tetration_mod(n, m)
    
    with open('output.txt', 'w') as f:
        f.write(str(result))

if __name__ == '__main__':
    main()
