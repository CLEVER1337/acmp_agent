
import sys

def main():
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    names = data[1:1+n]
    
    start_count = {}
    end_count = {}
    
    for name in names:
        first_char = name[:3]
        last_char = name[-3:]
        start_count[first_char] = start_count.get(first_char, 0) + 1
        end_count[last_char] = end_count.get(last_char, 0) + 1
    
    all_chars = set(start_count.keys()) | set(end_count.keys())
    
    balance = {}
    for char in all_chars:
        balance[char] = start_count.get(char, 0) - end_count.get(char, 0)
    
    positive = []
    negative = []
    
    for char, diff in balance.items():
        if diff > 0:
            positive.append((char, diff))
        elif diff < 0:
            negative.append((char, -diff))
    
    if not positive and not negative:
        print(0)
        return
        
    total_positive = sum(diff for _, diff in positive)
    total_negative = sum(diff for _, diff in negative)
    
    if total_positive == total_negative:
        print(total_positive)
    else:
        print(max(total_positive, total_negative))

if __name__ == "__main__":
    main()
