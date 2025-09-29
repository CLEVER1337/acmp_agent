
import sys

def sum_divisors(n):
    total = 1
    i = 2
    while i * i <= n:
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i
        i += 1
    return total

def main():
    with open('INPUT.TXT', 'r') as f:
        M, N = map(int, f.readline().split())
    
    pairs = []
    found_pairs = set()
    
    for a in range(M, N + 1):
        if a in found_pairs:
            continue
            
        b = sum_divisors(a)
        if b <= a or b < M or b > N:
            continue
            
        if sum_divisors(b) == a:
            pairs.append((a, b))
            found_pairs.add(a)
            found_pairs.add(b)
    
    if not pairs:
        with open('OUTPUT.TXT', 'w') as f:
            f.write("Absent")
    else:
        pairs.sort()
        with open('OUTPUT.TXT', 'w') as f:
            for a, b in pairs:
                f.write(f"{a} {b}\n")

if __name__ == "__main__":
    main()
