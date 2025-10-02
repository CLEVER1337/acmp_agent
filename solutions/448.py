
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
        n = int(f.read().strip())
    
    used = [False] * (n + 1)
    pairs = []
    
    for i in range(n, 0, -1):
        if not used[i]:
            for j in range(1, i):
                if not used[j] and is_prime(i + j):
                    pairs.append((j, i))
                    used[i] = True
                    used[j] = True
                    break
    
    with open('OUTPUT.TXT', 'w') as f:
        for pair in pairs:
            f.write(f"{pair[0]} {pair[1]}\n")

if __name__ == "__main__":
    main()
