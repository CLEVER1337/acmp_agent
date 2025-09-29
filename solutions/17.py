
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    numbers = list(map(int, data[1:1+n]))
    
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i+1] = prefix[i] + numbers[i]
    
    total_sum = prefix[n]
    
    def check(k):
        if total_sum % k != 0:
            return False
        
        target = total_sum // k
        count = 0
        current_sum = 0
        
        for i in range(n):
            current_sum += numbers[i]
            if current_sum == target:
                count += 1
                current_sum = 0
            elif current_sum > target:
                return False
        
        return count == k
    
    min_sectors = n
    for k in range(1, n//2 + 1):
        if n % k == 0 and check(k):
            min_sectors = min(min_sectors, n // k)
    
    print(min_sectors)

if __name__ == "__main__":
    main()
