
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

def generate_prime_string(max_pos):
    prime_str = ""
    n = 2
    while len(prime_str) < max_pos:
        if is_prime(n):
            prime_str += str(n)
        n += 1
    return prime_str

def main():
    import sys
    data = sys.stdin.read().split()
    m = int(data[0])
    positions = list(map(int, data[1:1+m]))
    
    max_pos = max(positions)
    prime_str = generate_prime_string(max_pos)
    
    result = ''.join(prime_str[pos-1] for pos in positions)
    print(result)

if __name__ == "__main__":
    main()
