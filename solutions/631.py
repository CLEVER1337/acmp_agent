
def main():
    with open('INPUT.TXT', 'r') as f:
        N = int(f.read().strip())
    
    if N == 0:
        result = 0
    else:
        low, high = 0, 100
        while high - low > 1:
            mid = (low + high) // 2
            if (1 << mid) >= N:
                high = mid
            else:
                low = mid
        
        k = high
        result = 2 * k - 1
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(result))

if __name__ == '__main__':
    main()
