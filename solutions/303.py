
def main():
    with open('INPUT.TXT', 'r') as f:
        num_str = f.read().strip()
    
    n = len(num_str)
    max_sum = float('-inf')
    
    for i in range(n):
        new_num = num_str[:i] + num_str[i+1:]
        current_sum = 0
        sign = 1
        
        for j, digit in enumerate(new_num):
            current_sum += sign * int(digit)
            sign *= -1
        
        if current_sum > max_sum:
            max_sum = current_sum
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(max_sum))

if __name__ == '__main__':
    main()
