
def main():
    import sys
    n = int(sys.stdin.readline().strip())
    if n == 1:
        print('0')
        return
    if n == 2:
        print('0 1')
        return
    if n <= 4:
        print('-1')
        return
        
    result = [0] * n
    left = 0
    right = n - 1
    num = 0
    
    while left <= right:
        if left == right:
            result[left] = num
            break
        result[left] = num
        num += 1
        result[right] = num
        num += 1
        left += 1
        right -= 1
        
    print(' '.join(map(str, result)))

if __name__ == '__main__':
    main()
