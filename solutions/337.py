
def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        print(0)
        return
        
    N = int(data[0])
    K = int(data[1])
    periods = list(map(int, data[2:2+K]))
    
    from math import gcd
    from functools import reduce
    
    def lcm(a, b):
        return a * b // gcd(a, b)
    
    def inclusion_exclusion(periods, N):
        periods = sorted(set(periods))
        m = len(periods)
        total = 0
        
        for i in range(1, 1 << m):
            bits = bin(i).count('1')
            current_lcm = 1
            for j in range(m):
                if i & (1 << j):
                    current_lcm = lcm(current_lcm, periods[j])
                    if current_lcm > N:
                        break
            if current_lcm > N:
                continue
                
            count = N // current_lcm
            if bits % 2 == 1:
                total += count
            else:
                total -= count
                
        return total
    
    result = inclusion_exclusion(periods, N)
    print(result)

if __name__ == "__main__":
    main()
