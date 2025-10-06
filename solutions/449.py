
def main():
    import sys
    data = sys.stdin.read().split()
    L = int(data[0])
    N = int(data[1])
    numbers = list(map(int, data[2:2+N]))
    
    numbers.sort()
    
    intervals = []
    for num in numbers:
        left = num - L
        right = num + L
        intervals.append((left, right))
    
    count = 0
    current_end = -10**9
    
    for left, right in intervals:
        if left > current_end:
            count += 1
            current_end = right
        else:
            current_end = min(current_end, right)
            
    print(count)

if __name__ == "__main__":
    main()
