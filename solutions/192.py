
def next_permutation(arr):
    n = len(arr)
    i = n - 2
    while i >= 0 and arr[i] >= arr[i + 1]:
        i -= 1
    
    if i == -1:
        return list(range(1, n + 1))
    
    j = n - 1
    while arr[j] <= arr[i]:
        j -= 1
    
    arr[i], arr[j] = arr[j], arr[i]
    
    left = i + 1
    right = n - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    
    return arr

def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    perm = list(map(int, data[1:1+n]))
    
    result = next_permutation(perm)
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(' '.join(map(str, result)))

if __name__ == "__main__":
    main()
