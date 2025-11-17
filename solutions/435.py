
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    k = int(data[1])
    
    if n == 1:
        print(0)
        return
        
    total_sequences = (k + 1) ** n
    half_max = 300 // 2
    dp = {}
    dp[(0, 0)] = 1
    
    for _ in range(n):
        new_dp = {}
        for (s, mask), count in dp.items():
            for d in range(k + 1):
                new_s = s + d
                shifted = mask << d
                new_mask = mask | shifted
                new_dp[(new_s, new_mask)] = new_dp.get((new_s, new_mask), 0) + count
        dp = new_dp
        
    lucky_count = 0
    for (s, mask), count in dp.items():
        if s > 0:
            if s % 2 == 0:
                half = s // 2
                if half < 300 and (mask & (1 << half)):
                    lucky_count += count
                    
    total_digits = 2**(n - 1) - 1
    unlucky_count = total_sequences - lucky_count - total_digits if n > 1 else total_sequences
    print(unlucky_count)

if __name__ == "__main__":
    main()
