
def main():
    n_str = input().strip()
    n = int(n_str)
    if n == 1:
        print('0')
        return
    if n == 2:
        print('0')
        return
    if n == 3:
        print('1')
        return
        
    length = 3
    k = 1
    while length < n:
        k += 1
        length = 2 * length + (2**k - 1)
        
    def find_bit(pos, level, invert):
        if level == 1:
            if pos == 1:
                return 0 if not invert else 1
            elif pos == 2:
                return 0 if not invert else 1
            else:
                return 1 if not invert else 0
                
        prev_len = (2**(level) - level - 1)
        middle_start = prev_len + 1
        middle_end = middle_start + (2**level - 1) - 1
        
        if pos <= prev_len:
            return find_bit(pos, level-1, invert)
        elif pos <= middle_end:
            return 1 if not invert else 0
        else:
            return find_bit(pos - middle_end, level-1, not invert)
            
    result = find_bit(n, k, False)
    print(str(result))

if __name__ == '__main__':
    main()
