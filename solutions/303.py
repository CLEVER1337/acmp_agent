
def main():
    with open('INPUT.TXT', 'r') as f:
        num_str = f.read().strip()
    
    n = len(num_str)
    max_sum = float('-inf')
    
    for i in range(n):
        new_num = num_str[:i] + num_str[i+1:]
        total = 0
        sign = 1
        
        for j, digit in enumerate(new_num):
            total += sign * int(digit)
            sign *= -1
        
        max_sum = max(max_sum, total)
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(max_sum))

if __name__ == '__main__':
    main()
