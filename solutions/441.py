
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    a_list = list(map(int, data[1:1+n]))
    b_list = list(map(int, data[1+n:1+2*n]))
    
    if sorted(a_list) != sorted(b_list):
        print(-1)
        return
        
    b_index = {}
    for idx, num in enumerate(b_list):
        if num not in b_index:
            b_index[num] = []
        b_index[num].append(idx)
    
    for key in b_index:
        b_index[key].sort(reverse=True)
    
    target_positions = []
    for num in a_list:
        pos = b_index[num].pop()
        target_positions.append(pos)
    
    inversions = 0
    temp = [0] * n
    
    def merge_count(left, right):
        nonlocal inversions
        i = j = 0
        merged = []
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
                inversions += len(left) - i
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged
    
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        return merge_count(left, right)
    
    merge_sort(target_positions)
    print(inversions)

if __name__ == "__main__":
    main()
