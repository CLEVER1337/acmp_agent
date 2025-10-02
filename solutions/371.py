
def sum_divisors(x):
    s = 1
    i = 2
    while i * i <= x:
        if x % i == 0:
            s += i
            if i != x // i:
                s += x // i
        i += 1
    return s

def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        return
    
    M = int(data[0])
    N = int(data[1])
    
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
    
    pairs.sort()
    
    if not pairs:
        print("Absent")
    else:
        for a, b in pairs:
            print(f"{a} {b}")

if __name__ == "__main__":
    main()
