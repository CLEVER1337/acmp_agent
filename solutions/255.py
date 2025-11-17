
import math

def main():
    n = int(input().strip())
    if n % 2 == 0:
        half = n // 2
        if half % 2 == 0:
            a = half - 1
            b = half + 1
        else:
            a = half
            b = half
    else:
        k = n // 2
        a = k
        b = n - k
        
    d = math.gcd(a, b)
    best_gcd = d
    best_a = a
    best_b = b
    
    divisors = set()
    num = n
    i = 1
    while i * i <= num:
        if num % i == 0:
            divisors.add(i)
            divisors.add(num // i)
        i += 1
    
    for d in divisors:
        if d >= n:
            continue
        candidate_a = d
        candidate_b = n - d
        if candidate_a > candidate_b:
            continue
        current_gcd = math.gcd(candidate_a, candidate_b)
        if current_gcd > best_gcd or (current_gcd == best_gcd and candidate_a < best_a):
            best_gcd = current_gcd
            best_a = candidate_a
            best_b = candidate_b
            
    print(f"{best_a} {best_b}")

if __name__ == "__main__":
    main()
