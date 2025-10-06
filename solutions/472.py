
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    m = int(data[1])
    arr = list(map(int, data[2:2+n]))
    
    arr.sort()
    total_added = 0
    
    for i in range(1, n):
        diff = arr[i] - arr[i-1]
        needed = diff * i
        if total_added + needed <= m:
            total_added += needed
        else:
            remaining = m - total_added
            add_per_bucket = remaining // i
            arr[i-1] += add_per_bucket
            total_added += add_per_bucket * i
            break
    else:
        remaining = m - total_added
        add_per_bucket = remaining // n
        arr[-1] += add_per_bucket
        total_added += add_per_bucket * n
        remaining -= add_per_bucket * n
        
    if total_added < m:
        remaining = m - total_added
        for i in range(remaining):
            arr[i % n] += 1
            
    result = min(arr)
    print(result)

if __name__ == "__main__":
    main()
