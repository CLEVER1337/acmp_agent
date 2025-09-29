
def main():
    with open('INPUT.TXT', 'r') as f:
        n_str = f.read().strip()
    
    n = int(n_str)
    
    if n == 1:
        result = '0'
    elif n == 2:
        result = '0'
    elif n == 3:
        result = '1'
    else:
        length = 3
        k = 1
        
        while length < n:
            k += 1
            length = 2 * length + (2 ** k - 1)
        
        offset = 0
        while k > 1:
            prev_len = (length - (2 ** k - 1)) // 2
            if n <= prev_len:
                length = prev_len
                k -= 1
            elif n <= 2 * prev_len:
                n -= prev_len
                length = prev_len
                k -= 1
            else:
                n -= 2 * prev_len
                offset += 2 ** k - 1
                length = prev_len
                k -= 1
        
        if n == 1:
            result = '0'
        elif n == 2:
            result = '0'
        elif n == 3:
            result = '1'
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(result)

if __name__ == '__main__':
    main()
