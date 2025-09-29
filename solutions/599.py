
import sys

def main():
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    s = data[1].split()
    
    arr = [ord(c) - ord('a') for c in s]
    
    prefix_sum = [0] * (n + 1)
    prefix_weighted = [0] * (n + 1)
    
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + arr[i]
        prefix_weighted[i + 1] = prefix_weighted[i] + i * arr[i]
    
    total_sum = prefix_sum[n]
    total_weighted = prefix_weighted[n]
    
    def f(i):
        left_sum = prefix_sum[i]
        left_weighted = prefix_weighted[i]
        right_sum = total_sum - left_sum
        right_weighted = total_weighted - left_weighted
        
        term1 = i * left_sum - left_weighted
        term2 = right_weighted - i * right_sum
        
        return term1 + term2
    
    max_score = -1
    best_index = -1
    
    for i in range(n):
        score = f(i)
        if score > max_score:
            max_score = score
            best_index = i
    
    print(max_score)
    print(best_index + 1)

if __name__ == "__main__":
    main()
