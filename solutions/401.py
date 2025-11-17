
import sys
from math import comb

def main():
    data = sys.stdin.read().split()
    if not data:
        print(0)
        return
    N = int(data[0])
    A = int(data[1])
    B = int(data[2])
    
    total_ways = 0
    for a_placed in range(A + 1):
        for b_placed in range(B + 1):
            ways_a = comb(a_placed + N - 1, N - 1) if a_placed > 0 else 1
            ways_b = comb(b_placed + N - 1, N - 1) if b_placed > 0 else 1
            total_ways += ways_a * ways_b
    
    print(total_ways)

if __name__ == "__main__":
    main()
