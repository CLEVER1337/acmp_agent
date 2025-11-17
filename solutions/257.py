
import sys
import math

def find_roots(a, b, c, d):
    if a == 0:
        if b == 0:
            if c == 0:
                if d == 0:
                    return -1, []
                else:
                    return 0, []
            else:
                x = -d / c
                if x.is_integer():
                    return 1, [int(x)]
                else:
                    return 0, []
        else:
            disc = c * c - 4 * b * d
            if disc < 0:
                return 0, []
            elif disc == 0:
                x = -c / (2 * b)
                if x.is_integer():
                    return 1, [int(x)]
                else:
                    return 0, []
            else:
                root1 = (-c - math.isqrt(disc)) / (2 * b)
                root2 = (-c + math.isqrt(disc)) / (2 * b)
                roots = []
                if root1.is_integer():
                    roots.append(int(root1))
                if root2.is_integer():
                    roots.append(int(root2))
                roots = sorted(list(set(roots)))
                return len(roots), roots
    else:
        roots = set()
        for p in divisors(abs(d)) if d != 0 else [0]:
            for candidate in [p, -p]:
                if a * candidate**3 + b * candidate**2 + c * candidate + d == 0:
                    roots.add(candidate)
        if len(roots) > 3:
            roots = sorted(list(roots))
            return len(roots), roots
        a1 = a
        b1 = b + a * next(iter(roots)) if roots else b
        c1 = c + b1 * next(iter(roots)) if roots else c
        remaining_roots = set()
        if roots:
            r0 = next(iter(roots))
            discriminant = b1 * b1 - 4 * a1 * c1
            if discriminant < 0:
                pass
            elif discriminant == 0:
                root_val = -b1 / (2 * a1)
                if root_val.is_integer():
                    remaining_roots.add(int(root_val))
            else:
                root1 = (-b1 - math.isqrt(discriminant)) / (2 * a1)
                root2 = (-b1 + math.isqrt(discriminant)) / (2 * a1)
                if root1.is_integer():
                    remaining_roots.add(int(root1))
                if root2.is_integer():
                    remaining_roots.add(int(root2))
        all_roots = roots.union(remaining_roots)
        all_roots = sorted(list(all_roots))
        return len(all_roots), all_roots

def divisors(n):
    if n == 0:
        yield 0
        return
    divs = set()
    for i in range(1, int(math.isqrt(n)) + 1):
        if n % i == 0:
            divs.add(i)
            divs.add(n // i)
    yield from divs

def main():
    data = sys.stdin.read().split()
    if not data:
        print(0)
        return
    a = int(data[0])
    b = int(data[1])
    c = int(data[2])
    d = int(data[3])
    
    if a == 0 and b == 0 and c == 0 and d == 0:
        print(-1)
        return
        
    count, roots = find_roots(a, b, c, d)
    if count == -1:
        print(-1)
    else:
        print(count)
        if count > 0:
            print(' '.join(map(str, roots)))
            
if __name__ == "__main__":
    main()
