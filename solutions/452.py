
def main():
    with open('INPUT.TXT', 'r') as f:
        a_str = f.readline().strip()
        b_str = f.readline().strip()
    
    max_len = max(len(a_str), len(b_str))
    a_str = a_str.zfill(max_len)
    b_str = b_str.zfill(max_len)
    
    fib_weights = []
    f1, f2 = 1, 2
    for _ in range(max_len):
        fib_weights.append(f1)
        f1, f2 = f2, f1 + f2
    
    a_num = 0
    for i, digit in enumerate(a_str[::-1]):
        if digit == '1':
            a_num += fib_weights[i]
    
    b_num = 0
    for i, digit in enumerate(b_str[::-1]):
        if digit == '1':
            b_num += fib_weights[i]
    
    sum_num = a_num + b_num
    
    max_fib = fib_weights[-1] + fib_weights[-2]
    while max_fib <= sum_num:
        fib_weights.append(max_fib)
        max_fib = fib_weights[-1] + fib_weights[-2]
    
    result = []
    for weight in reversed(fib_weights):
        if sum_num >= weight:
            result.append('1')
            sum_num -= weight
        else:
            result.append('0')
    
    result_str = ''.join(result).lstrip('0')
    if not result_str:
        result_str = '0'
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(result_str)

if __name__ == "__main__":
    main()
