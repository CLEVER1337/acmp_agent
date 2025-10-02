
def count_combinations(n, k):
    if k < 0 or k > n:
        return 0
    res = 1
    for i in range(1, k + 1):
        res = res * (n - k + i) // i
    return res

def find_nth_smooth_number(N):
    length = 1
    total = 0
    
    while True:
        count = count_combinations(9 + length, length)
        if total + count >= N:
            break
        total += count
        length += 1
    
    pos = N - total
    result = []
    prev_digit = 0
    
    for i in range(length):
        for digit in range(prev_digit, 10):
            remaining_length = length - len(result) - 1
            count = count_combinations(9 - digit + remaining_length, remaining_length)
            if pos <= count:
                result.append(str(digit))
                prev_digit = digit
                break
            pos -= count
    
    return ''.join(result)

def main():
    with open('INPUT.TXT', 'r') as f:
        N = int(f.read().strip())
    result = find_nth_smooth_number(N)
    with open('OUTPUT.TXT', 'w') as f:
        f.write(result)

if __name__ == '__main__':
    main()
