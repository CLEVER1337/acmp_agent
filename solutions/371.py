
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        print("Absent")
        return
        
    M = int(data[0])
    N = int(data[1])
    
    def sum_divisors(x):
        total = 1
        i = 2
        while i * i <= x:
            if x % i == 0:
                total += i
                if i != x // i:
                    total += x // i
            i += 1
        return total
    
    pairs = []
    checked = set()
    
    for a in range(M, N + 1):
        if a in checked:
            continue
            
        b = sum_divisors(a)
        if b <= a or b < M or b > N:
            continue
            
        if sum_divisors(b) == a:
            pairs.append((a, b))
            checked.add(b)
    
    if not pairs:
        print("Absent")
    else:
        pairs.sort()
        for a, b in pairs:
            print(f"{a} {b}")

if __name__ == "__main__":
    main()
