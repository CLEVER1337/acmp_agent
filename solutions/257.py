
import math

def find_roots(a, b, c, d):
    if a == 0:
        if b == 0:
            if c == 0:
                if d == 0:
                    return -1, []  # Бесконечно много корней
                else:
                    return 0, []   # Нет корней
            else:
                # Линейное уравнение: c*x + d = 0
                if d % c == 0:
                    root = -d // c
                    return 1, [root]
                else:
                    return 0, []
        else:
            # Квадратное уравнение: b*x^2 + c*x + d = 0
            discriminant = c*c - 4*b*d
            if discriminant < 0:
                return 0, []
            elif discriminant == 0:
                if c % (2*b) == 0:
                    root = -c // (2*b)
                    return 1, [root]
                else:
                    return 0, []
            else:
                sqrt_disc = math.isqrt(discriminant)
                if sqrt_disc * sqrt_disc != discriminant:
                    return 0, []
                
                roots = set()
                numerator1 = -c + sqrt_disc
                numerator2 = -c - sqrt_disc
                denominator = 2 * b
                
                if numerator1 % denominator == 0:
                    roots.add(numerator1 // denominator)
                if numerator2 % denominator == 0:
                    roots.add(numerator2 // denominator)
                
                return len(roots), sorted(roots)
    else:
        # Кубическое уравнение
        roots = set()
        
        # Ищем целые корни среди делителей свободного члена
        divisors = set()
        d_abs = abs(d)
        for i in range(1, int(math.sqrt(d_abs)) + 1):
            if d_abs % i == 0:
                divisors.add(i)
                divisors.add(d_abs // i)
                divisors.add(-i)
                divisors.add(-d_abs // i)
        divisors.add(0) if d == 0 else None
        
        for x in divisors:
            if a*x*x*x + b*x*x + c*x + d == 0:
                roots.add(x)
        
        return len(roots), sorted(roots)

def main():
    with open('INPUT.TXT', 'r') as f:
        data = f.read().split()
        if not data:
            return
        a, b, c, d = map(int, data)
    
    count, roots = find_roots(a, b, c, d)
    
    with open('OUTPUT.TXT', 'w') as f:
        if count == -1:
            f.write('-1')
        else:
            f.write(f"{count}\n")
            if roots:
                f.write(' '.join(map(str, roots)))

if __name__ == '__main__':
    main()
