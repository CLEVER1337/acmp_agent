
import sys

def find_digit(n):
    length = 1
    count = 9
    start = 1
    
    while n > length * count:
        n -= length * count
        length += 1
        count *= 10
        start *= 10
        
    start += (n - 1) // length
    digit_index = (n - 1) % length
    return int(str(start)[digit_index])

def main():
    data = sys.stdin.read().split()
    t = int(data[0])
    results = []
    index = 1
    
    for _ in range(t):
        k = int(data[index])
        p = int(data[index + 1])
        index += 2
        
        if p == 1:
            if k <= 9:
                results.append(str(k))
            else:
                results.append("No solution")
        else:
            left, right = 1, 10**18
            found = False
            
            while left <= right:
                mid = (left + right) // 2
                total_digits = 0
                current = 1
                count = 9
                length = 1
                
                while current <= mid:
                    next_val = min(mid, current * 10 - 1)
                    block_length = next_val - current + 1
                    total_digits += block_length * length
                    current *= 10
                    length += 1
                
                if total_digits < k:
                    left = mid + 1
                else:
                    right = mid - 1
                    candidate = mid
            
            if left > 10**18:
                results.append("No solution")
                continue
                
            total_digits_before = 0
            current = 1
            count = 9
            length = 1
            
            while current <= candidate - 1:
                next_val = min(candidate - 1, current * 10 - 1)
                block_length = next_val - current + 1
                total_digits_before += block_length * length
                current *= 10
                length += 1
            
            remaining_digits = k - total_digits_before
            number = candidate
            num_str = str(number)
            
            if remaining_digits <= len(num_str):
                digit = int(num_str[remaining_digits - 1])
                if digit % p == 0:
                    results.append(str(digit))
                else:
                    results.append("No solution")
            else:
                results.append("No solution")
    
    sys.stdout.write("\n".join(results))

if __name__ == "__main__":
    main()
