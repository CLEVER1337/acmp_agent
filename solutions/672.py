
def main():
    n = int(input().strip())
    if n == 1:
        print("10 0")
        return
        
    from itertools import product
    
    count = 0
    min_num = float('inf')
    
    digits = list(range(1, 10))
    zeros = list(range(0, 10))
    
    for num_digits in product(digits, repeat=n):
        total_sum = sum(num_digits)
        product_val = 1
        for d in num_digits:
            product_val *= d
            if product_val == 0:
                break
                
        if product_val == 0:
            continue
            
        if total_sum == product_val:
            num = int(''.join(map(str, num_digits)))
            count += 1
            if num < min_num:
                min_num = num
                
    if count == 0:
        print("0 0")
    else:
        print(f"{count} {min_num}")

if __name__ == "__main__":
    main()
