
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    an = int(data[1])
    an1 = int(data[2])
    
    if n == 1:
        print(an, an1)
        return
        
    fib = [0] * (n + 2)
    fib[0] = (1, 0)
    fib[1] = (0, 1)
    
    for i in range(2, n + 1):
        fib[i] = (fib[i-1][0] + fib[i-2][0], fib[i-1][1] + fib[i-2][1])
    
    coeff_n = fib[n-1]
    coeff_n1 = fib[n]
    
    a = coeff_n[0]
    b = coeff_n[1]
    c = coeff_n1[0]
    d = coeff_n1[1]
    
    for a2 in range(-2000000000, 2000000001):
        numerator = an - b * a2
        if numerator % a != 0:
            continue
        a1 = numerator // a
        
        if a1 * c + a2 * d == an1:
            if -2000000000 <= a1 <= 2000000000:
                print(a1, a2)
                return
                
    for a1 in range(-2000000000, 2000000001):
        numerator = an1 - d * a1
        if numerator % c != 0:
            continue
        a2 = numerator // c
        
        if a1 * a + a2 * b == an:
            if -2000000000 <= a2 <= 2000000000:
                print(a1, a2)
                return
