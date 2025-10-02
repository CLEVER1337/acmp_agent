
def main():
    import sys
    data = sys.stdin.readline().split()
    N = int(data[0])
    M = int(data[1])
    
    if M == 1:
        print(N)
        return
        
    result = 0
    left, right = 1, N
    while left <= right:
        mid = (left + right) // 2
        eliminated = mid
        remaining = N - eliminated
        
        position = 1
        step = 1
        while step <= remaining:
            if position >= M:
                break
            position += step
            step *= 2
            
        if position < M:
            left = mid + 1
        else:
            result = mid
            right = mid - 1
            
    print(result)

if __name__ == "__main__":
    main()
