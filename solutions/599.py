
import sys

def main():
    data = sys.stdin.read().splitlines()
    n = int(data[0].strip())
    s = data[1].strip().replace(' ', '')
    
    arr = [ord(c) - ord('a') for c in s]
    total_len = n
    
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + arr[i]
    
    prefix_sq = [0] * (n + 1)
    for i in range(n):
        prefix_sq[i + 1] = prefix_sq[i] + arr[i] * i
    
    def get_sum(l, r):
        if l <= r:
            return prefix[r + 1] - prefix[l]
        else:
            return prefix[r + 1] + (prefix[n] - prefix[l])
    
    def get_sum_sq(l, r):
        if l <= r:
            return prefix_sq[r + 1] - prefix_sq[l]
        else:
            return prefix_sq[r + 1] + (prefix_sq[n] - prefix_sq[l])
    
    def f(i):
        left = (i - total_len // 2) % total_len
        right = (i + total_len // 2) % total_len
        
        if left < 0:
            left += total_len
        
        if left < i:
            part1 = get_sum_sq(left, i) - get_sum(left, i) * left
            part2 = get_sum(i, right) * (total_len - i) - (get_sum_sq(i, right) - get_sum(i, right) * i)
        else:
            part1 = get_sum_sq(left, n - 1) - get_sum(left, n - 1) * left + get_sum_sq(0, i) + get_sum(0, i) * (total_len - left)
            part2 = get_sum(i, n - 1) * (total_len - i) - (get_sum_sq(i, n - 1) - get_sum(i, n - 1) * i) + get_sum(0, right) * (total_len - i) - (get_sum_sq(0, right) + get_sum(0, right) * (total_len - i))
        
        return part1 + part2
    
    max_val = -1
    best_index = -1
    
    for i in range(n):
        current = f(i)
        if current > max_val:
            max_val = current
            best_index = i
    
    print(max_val)
    print(best_index + 1)

if __name__ == "__main__":
    main()
