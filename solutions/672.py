
def main():
    with open('INPUT.TXT', 'r') as f:
        N = int(f.readline().strip())
    
    if N == 1:
        count = 1
        min_num = 0
    else:
        count = 0
        min_num = None
        
        start = 10**(N-1)
        end = 10**N
        
        for num in range(start, end):
            digits = [int(d) for d in str(num)]
            sum_digits = sum(digits)
            prod_digits = 1
            for d in digits:
                prod_digits *= d
            
            if sum_digits == prod_digits:
                count += 1
                if min_num is None or num < min_num:
                    min_num = num
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(f"{count} {min_num}")

if __name__ == "__main__":
    main()
