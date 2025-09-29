
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    m = int(data[1])
    index = 2
    
    starts = []
    ends = []
    
    for i in range(n):
        a = int(data[index])
        b = int(data[index + 1])
        index += 2
        start = min(a, b)
        end = max(a, b)
        starts.append(start)
        ends.append(end)
    
    points = list(map(int, data[index:index + m]))
    
    starts.sort()
    ends.sort()
    
    result = []
    for point in points:
        left_count = binary_search_right(starts, point)
        right_count = binary_search_left(ends, point)
        result.append(str(left_count - right_count))
    
    print(' '.join(result))

def binary_search_right(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return left

def binary_search_left(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left

if __name__ == "__main__":
    main()
