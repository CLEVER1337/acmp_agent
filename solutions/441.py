
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    a = list(map(int, data[1:1+n]))
    b = list(map(int, data[1+n:1+2*n]))
    
    if sorted(a) != sorted(b):
        print(-1)
        return
        
    pos_in_b = {}
    for idx, num in enumerate(b):
        pos_in_b[num] = idx
        
    target_indices = [pos_in_b[x] for x in a]
    
    inversions = 0
    temp = [0] * n
    
    def merge_sort(arr, left, right):
        nonlocal inversions
        if left >= right:
            return
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid+1, right)
        merge(arr, left, mid, right)
    
    def merge(arr, left, mid, right):
        nonlocal inversions, temp
        i, j, k = left, mid+1, left
        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp[k] = arr[i]
                i += 1
            else:
                temp[k] = arr[j]
                j += 1
                inversions += (mid - i + 1)
            k += 1
        
        while i <= mid:
            temp[k] = arr[i]
            i += 1
            k += 1
        
        while j <= right:
            temp[k] = arr[j]
            j += 1
            k += 1
        
        for idx in range(left, right+1):
            arr[idx] = temp[idx]
    
    merge_sort(target_indices, 0, n-1)
    print(inversions)

if __name__ == "__main__":
    main()
