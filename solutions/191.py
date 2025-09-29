
def count_combinations(n, k):
    if k < 0 or k > n:
        return 0
    res = 1
    for i in range(1, k + 1):
        res = res * (n - k + i) // i
    return res

def find_nth_smooth_number(n):
    length = 1
    while True:
        count = count_combinations(9 + length, length)
        if n <= count:
            break
        n -= count
        length += 1
    
    result = []
    prev_digit = 1
    
    for pos in range(length):
        for digit in range(prev_digit, 10):
            remaining_positions = length - pos - 1
            combinations = count_combinations(10 - digit, remaining_positions)
            if n <= combinations:
                result.append(str(digit))
                prev_digit = digit
                break
            n -= combinations
    
    return ''.join(result)

def main():
    with open('INPUT.TXT', 'r') as f:
        n = int(f.read().strip())
    result = find_nth_smooth_number(n)
    with open('OUTPUT.TXT', 'w') as f:
        f.write(result)

if __name__ == '__main__':
    main()
