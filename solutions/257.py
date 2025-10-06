
import math

def main():
    with open('INPUT.TXT', 'r') as f:
        data = f.read().split()
        A = int(data[0])
        B = int(data[1])
        C = int(data[2])
        D = int(data[3])
    
    if A == 0 and B == 0 and C == 0:
        if D == 0:
            print(-1)
        else:
            print(0)
        return
    
    if A == 0 and B == 0:
        x = -D / C
        if x.is_integer():
            print(1)
            print(int(x))
        else:
            print(0)
        return
    
    if A == 0:
        discriminant = C * C - 4 * B * D
        if discriminant < 0:
            print(0)
            return
        elif discriminant == 0:
            x = -C / (2 * B)
            if x.is_integer():
                print(1)
                print(int(x))
            else:
                print(0)
        else:
            sqrt_discr = math.isqrt(discriminant)
            if sqrt_discr * sqrt_discr != discriminant:
                print(0)
                return
            
            x1 = (-C - sqrt_discr) / (2 * B)
            x2 = (-C + sqrt_discr) / (2 * B)
            roots = set()
            if x1.is_integer():
                roots.add(int(x1))
            if x2.is_integer():
                roots.add(int(x2))
            
            roots = sorted(roots)
            print(len(roots))
            for root in roots:
                print(root)
        return
    
    def f(x):
        return A * x * x * x + B * x * x + C * x + D
    
    roots = set()
    divisors_D = set()
    divisors_A = set()
    
    d_abs = abs(D)
    a_abs = abs(A)
    
    for i in range(1, int(math.isqrt(d_abs)) + 1):
        if d_abs % i == 0:
            divisors_D.add(i)
            divisors_D.add(-i)
            divisors_D.add(d_abs // i)
            divisors_D.add(-(d_abs // i))
    
    for i in range(1, int(math.isqrt(a_abs)) + 1):
        if a_abs % i == 0:
            divisors_A.add(i)
            divisors_A.add(-i)
            divisors_A.add(a_abs // i)
            divisors_A.add(-(a_abs // i))
    
    divisors_D.add(0)
    
    candidates = set()
    for p in divisors_D:
        for q in divisors_A:
            if q != 0:
                candidate = p / q
                if candidate.is_integer():
                    candidates.add(int(candidate))
                else:
                    candidates.add(candidate)
    
    for candidate in candidates:
        if isinstance(candidate, int) and f(candidate) == 0:
            roots.add(candidate)
    
    roots = sorted(roots)
    print(len(roots))
    for root in roots:
        print(root)

if __name__ == "__main__":
    main()
