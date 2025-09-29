
def main():
    with open('INPUT.TXT', 'r') as f:
        N = int(f.readline().strip())
    
    if N == 0:
        result = 0
    else:
        left, right = 0, N
        while left < right:
            mid = (left + right) // 2
            if (1 << mid) >= N:
                right = mid
            else:
                left = mid + 1
        
        k = left
        result = 0
        for i in range(k, -1, -1):
            if N >= (1 << i):
                result += 2 * (1 << i)
                N -= (1 << i)
            else:
                result += 2 * N
                break
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(result))

if __name__ == '__main__':
    main()
