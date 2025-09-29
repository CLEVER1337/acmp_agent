
import math

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y

def solve_congruence(a, b, m):
    gcd, x0, _ = extended_gcd(a, m)
    if b % gcd != 0:
        return None
    x0 = (x0 * (b // gcd)) % m
    step = m // gcd
    return x0, step

def main():
    with open('INPUT.TXT', 'r') as f:
        a, b, c, d, e, f_val = map(int, f.read().split())
    
    gcd1, x1, y1 = extended_gcd(a, c)
    gcd2, x2, y2 = extended_gcd(d, f_val)
    
    if b % gcd1 != 0 or e % gcd2 != 0:
        print("NO")
        return
    
    sol1 = solve_congruence(a, b, c)
    sol2 = solve_congruence(d, e, f_val)
    
    if sol1 is None or sol2 is None:
        print("NO")
        return
    
    x0_1, step1 = sol1
    x0_2, step2 = sol2
    
    gcd_step = math.gcd(step1, step2)
    diff = (x0_2 - x0_1) % gcd_step
    
    if diff % gcd_step == 0:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
