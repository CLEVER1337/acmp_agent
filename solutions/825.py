
import math

def find_kth_losing_position(k):
    if k == 0:
        return (0, 0)
    
    n = int((math.isqrt(1 + 8 * k) - 1) // 2)
    remaining = k - n * (n + 1) // 2
    a = n - remaining
    b = n + 1 + remaining
    return (a, b)

def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    results = []
    for i in range(1, n + 1):
        k = int(data[i])
        a, b = find_kth_losing_position(k)
        results.append(f"{a} {b}")
    
    for res in results:
        print(res)

if __name__ == "__main__":
    main()
