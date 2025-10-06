
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    inv = list(map(int, data[1:1+n]))
    
    arr = [0] * n
    for i in range(n-1, -1, -1):
        count = inv[i]
        pos = i
        for j in range(i+1, n):
            if arr[j] >= i+1 - count:
                arr[j] += 1
            else:
                if arr[j] > arr[pos]:
                    pos = j
        arr[i] = i+1 - count
        
    print(' '.join(map(str, arr)))

if __name__ == "__main__":
    main()
