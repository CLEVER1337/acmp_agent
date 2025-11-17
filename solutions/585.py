
def binary_search(n):
    left, right = 0, n
    while left < right:
        mid = (left + right) // 2
        if 2 ** mid == n:
            return mid
        elif 2 ** mid < n:
            left = mid + 1
        else:
            right = mid - 1
    return -1

if __name__ == '__main__':
    with open('INPUT.TXT', 'r') as f:
        n = int(f.read().strip())
    result = binary_search(n)
    with open('OUTPUT.TXT', 'w') as f:
        if result == -1:
            f.write("-1")
        else:
            f.write(str(result))
