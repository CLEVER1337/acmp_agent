
import sys
from collections import Counter

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    nums = list(map(int, data[1:1+n]))
    
    counter = Counter(nums)
    
    max_count = 0
    candidate = None
    
    for num, count in counter.items():
        if count > max_count:
            max_count = count
            candidate = num
        elif count == max_count:
            if num < candidate:
                candidate = num
    
    result = []
    to_move = []
    
    for num in nums:
        if num == candidate:
            to_move.append(num)
        else:
            result.append(num)
    
    result.extend(to_move)
    
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()
