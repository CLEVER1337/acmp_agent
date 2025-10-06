
def main():
    n = int(input().strip())
    if n == 1:
        print(1)
        return
        
    left = 1
    right = 10**12
    while left < right:
        mid = (left + right) // 2
        count = 0
        k = 1
        while k * k <= mid:
            count += (mid // k) - (k - 1)
            k += 1
        if count < n:
            left = mid + 1
        else:
            right = mid
            
    print(left)

if __name__ == "__main__":
    main()
