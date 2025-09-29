
import math

def find_cubes(n):
    max_cube = int(math.isqrt(n))
    if max_cube * max_cube > n:
        max_cube -= 1
    max_cube = min(max_cube, 1290)
    
    for a in range(max_cube, 0, -1):
        a3 = a * a * a
        if a3 > n:
            continue
        if a3 == n:
            return [a]
        for b in range(min(a, int((n - a3) ** (1/3)) + 1), 0, -1):
            b3 = b * b * b
            if a3 + b3 > n:
                continue
            if a3 + b3 == n:
                return [a, b]
            for c in range(min(b, int((n - a3 - b3) ** (1/3)) + 1), 0, -1):
                c3 = c * c * c
                if a3 + b3 + c3 > n:
                    continue
                if a3 + b3 + c3 == n:
                    return [a, b, c]
                for d in range(min(c, int((n - a3 - b3 - c3) ** (1/3)) + 1), 0, -1):
                    d3 = d * d * d
                    if a3 + b3 + c3 + d3 > n:
                        continue
                    if a3 + b3 + c3 + d3 == n:
                        return [a, b, c, d]
                    for e in range(min(d, int((n - a3 - b3 - c3 - d3) ** (1/3)) + 1), 0, -1):
                        e3 = e * e * e
                        if a3 + b3 + c3 + d3 + e3 > n:
                            continue
                        if a3 + b3 + c3 + d3 + e3 == n:
                            return [a, b, c, d, e]
                        for f in range(min(e, int((n - a3 - b3 - c3 - d3 - e3) ** (1/3)) + 1), 0, -1):
                            f3 = f * f * f
                            if a3 + b3 + c3 + d3 + e3 + f3 > n:
                                continue
                            if a3 + b3 + c3 + d3 + e3 + f3 == n:
                                return [a, b, c, d, e, f]
                            for g in range(min(f, int((n - a3 - b3 - c3 - d3 - e3 - f3) ** (1/3)) + 1), 0, -1):
                                g3 = g * g * g
                                if a3 + b3 + c3 + d3 + e3 + f3 + g3 > n:
                                    continue
                                if a3 + b3 + c3 + d3 + e3 + f3 + g3 == n:
                                    return [a, b, c, d, e, f, g]
                                for h in range(min(g, int((n - a3 - b3 - c3 - d3 - e3 - f3 - g3) ** (1/3)) + 1), 0, -1):
                                    h3 = h * h * h
                                    if a3 + b3 + c3 + d3 + e3 + f3 + g3 + h3 == n:
                                        return [a, b, c, d, e, f, g, h]
    return None

def main():
    with open('INPUT.TXT', 'r') as f:
        n = int(f.read().strip())
    
    result = find_cubes(n)
    
    with open('OUTPUT.TXT', 'w') as f:
        if result:
            result.sort(reverse=True)
            f.write(' '.join(map(str, result)))
        else:
            f.write('IMPOSSIBLE')

if __name__ == '__main__':
    main()
