
def main():
    with open('INPUT.TXT', 'r') as f:
        n = int(f.readline().strip())
    
    if n == 1:
        count = 9
        smallest = 1
    else:
        from itertools import combinations_with_replacement
        count = 0
        smallest = float('inf')
        
        for digits in combinations_with_replacement(range(1, 10), n):
            sum_d = sum(digits)
            prod_d = 1
            for d in digits:
                prod_d *= d
            
            if sum_d == prod_d:
                count += 1
                num = int(''.join(map(str, sorted(digits))))
                if num < smallest:
                    smallest = num
        
        if count == 0:
            smallest = 0
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(f"{count} {smallest}")

if __name__ == '__main__':
    main()
