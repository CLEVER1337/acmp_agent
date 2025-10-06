
import sys

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def main():
    n = int(sys.stdin.readline().strip())
    used = [False] * (n + 1)
    pairs = []
    
    max_prime = 2 * n
    primes = []
    for num in range(2, max_prime + 1):
        if is_prime(num):
            primes.append(num)
    
    for p in reversed(primes):
        if p < 3:
            continue
        if p > n + n:
            continue
            
        start = max(1, p - n)
        end = min(n, p - 1)
        
        for i in range(start, end + 1):
            j = p - i
            if j < 1 or j > n:
                continue
            if not used[i] and not used[j] and i != j:
                used[i] = True
                used[j] = True
                pairs.append((i, j))
                break
    
    for i in range(1, n + 1):
        if not used[i] and i * 2 in primes:
            used[i] = True
            pairs.append((i, i))
            break
    
    for i in range(1, n + 1):
        if not used[i]:
            for j in range(i + 1, n + 1):
                if not used[j]:
                    s = i + j
                    if is_prime(s):
                        used[i] = True
                        used[j] = True
                        pairs.append((i, j))
                        break
    
    for pair in pairs:
        sys.stdout.write(f"{pair[0]} {pair[1]}\n")

if __name__ == "__main__":
    main()
