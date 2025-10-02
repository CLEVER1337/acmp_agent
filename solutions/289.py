
def main():
    D = int(input().strip())
    if D == 1:
        print(1)
        return
    
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
    exponents = [0] * len(primes)
    
    def backtrack(pos, divisors, current, limit):
        if divisors == D:
            return current
        if divisors > D or pos >= len(primes):
            return float('inf')
        
        best = float('inf')
        for e in range(1, limit + 1):
            if divisors * (e + 1) > D:
                break
            if current * primes[pos] ** e > 10**15 + 1:
                break
                
            next_val = backtrack(pos + 1, divisors * (e + 1), current * primes[pos] ** e, e)
            if next_val < best:
                best = next_val
                
        return best
    
    result = backtrack(0, 1, 1, 60)
    print(result if result <= 10**15 + 1 else 0)

if __name__ == "__main__":
    main()
