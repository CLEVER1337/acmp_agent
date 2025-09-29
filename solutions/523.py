
def main():
    with open('INPUT.TXT', 'r') as f:
        n = int(f.readline().strip())
        pages = list(map(int, f.readline().split()))
        k = int(f.readline().strip())
    
    left = max(pages)
    right = sum(pages)
    
    while left < right:
        mid = (left + right) // 2
        volumes = 1
        current_sum = 0
        
        for page in pages:
            if current_sum + page > mid:
                volumes += 1
                current_sum = page
            else:
                current_sum += page
        
        if volumes <= k:
            right = mid
        else:
            left = mid + 1
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(left))

if __name__ == '__main__':
    main()
