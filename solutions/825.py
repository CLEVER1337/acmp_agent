
import math

def find_kth_losing_pair(k):
    if k == 0:
        return (0, 0)
    
    phi = (1 + math.sqrt(5)) / 2
    n = math.floor(math.sqrt(2 * k))
    
    while True:
        start_index = n * (n + 1) // 2
        if start_index <= k:
            n += 1
        else:
            n -= 1
            break
    
    remaining = k - n * (n + 1) // 2
    a = n - remaining
    b = n + 1 + remaining
    
    return (a, b)

def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    results = []
    
    for i in range(n):
        k = int(data[i + 1])
        a, b = find_kth_losing_pair(k)
        results.append(f"{a} {b}")
    
    print("\n".join(results))

if __name__ == "__main__":
    main()
