
import sys

def main():
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    letters = data[1].split()
    
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    char_to_num = {char: idx for idx, char in enumerate(alphabet)}
    nums = [char_to_num[c] for c in letters]
    
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + nums[i]
    
    prefix_sum_sq = [0] * (n + 1)
    for i in range(n):
        prefix_sum_sq[i + 1] = prefix_sum_sq[i] + nums[i] * nums[i]
    
    def get_sum(l, r):
        if l <= r:
            return prefix_sum[r + 1] - prefix_sum[l]
        else:
            return prefix_sum[n] - prefix_sum[l] + prefix_sum[r + 1]
    
    def get_sum_sq(l, r):
        if l <= r:
            return prefix_sum_sq[r + 1] - prefix_sum_sq[l]
        else:
            return prefix_sum_sq[n] - prefix_sum_sq[l] + prefix_sum_sq[r + 1]
    
    max_score = -1
    best_index = -1
    
    for i in range(n):
        total = 0
        left_end = (i - n // 2) % n
        right_end = (i + n // 2) % n
        
        if n % 2 == 0:
            left_count = n // 2
            right_count = n // 2
        else:
            left_count = n // 2
            right_count = n // 2
        
        if left_end <= i:
            left_sum = get_sum(left_end, i - 1)
            left_sum_sq = get_sum_sq(left_end, i - 1)
            left_total = left_count * nums[i] - left_sum
            left_total += (nums[i] * left_sum - left_sum_sq)
        else:
            left_sum1 = get_sum(left_end, n - 1)
            left_sum2 = get_sum(0, i - 1)
            left_sum = left_sum1 + left_sum2
            
            left_sum_sq1 = get_sum_sq(left_end, n - 1)
            left_sum_sq2 = get_sum_sq(0, i - 1)
            left_sum_sq = left_sum_sq1 + left_sum_sq2
            
            left_total = left_count * nums[i] - left_sum
            left_total += (nums[i] * left_sum - left_sum_sq)
        
        if i < right_end:
            right_sum = get_sum(i + 1, right_end)
            right_sum_sq = get_sum_sq(i + 1, right_end)
            right_total = right_sum - right_count * nums[i]
            right_total += (right_sum_sq - nums[i] * right_sum)
        else:
            right_sum1 = get_sum(i + 1, n - 1)
            right_sum2 = get_sum(0, right_end)
            right_sum = right_sum1 + right_sum2
            
            right_sum_sq1 = get_sum_sq(i + 1, n - 1)
            right_sum_sq2 = get_sum_sq(0, right_end)
            right_sum_sq = right_sum_sq1 + right_sum_sq2
            
            right_total = right_sum - right_count * nums[i]
            right_total += (right_sum_sq - nums[i] * right_sum)
        
        total = left_total + right_total
        
        if total > max_score:
            max_score = total
            best_index = i + 1
    
    print(max_score)
    print(best_index)

if __name__ == "__main__":
    main()
