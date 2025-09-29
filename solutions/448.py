
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def main():
    with open('INPUT.TXT', 'r') as f:
        N = int(f.read().strip())
    
    pairs = []
    used = [False] * (N + 1)
    
    primes = []
    for num in range(2, 2 * N + 1):
        if is_prime(num):
            primes.append(num)
    
    for p in primes:
        if p > N + 1:
            break
        for i in range(1, N + 1):
            if i >= p:
                break
            j = p - i
            if j > N:
                continue
            if not used[i] and not used[j] and i != j:
                pairs.append((i, j))
                used[i] = True
                used[j] = True
    
    with open('OUTPUT.TXT', 'w') as f:
        for pair in pairs:
            f.write(f"{pair[0]} {pair[1]}\n")

if __name__ == '__main__':
    main()
