
def main():
    code_N_str = input().strip()
    K = int(input().strip())
    total_len = len(code_N_str)
    code_N = int(code_N_str)
    
    low_bound = 10**K + 1
    if code_N < low_bound:
        print("")
        return
        
    left_part_min = 10**(K-1)
    left_part_max = 10**K - 1
    
    def cyclic(n_str, k):
        if len(n_str) <= k:
            return int(n_str)
        left = n_str[:k]
        right = n_str[k:]
        shifted = right + left
        return int(shifted)
    
    low = 10**(total_len - 1)
    high = min(code_N, 10**total_len - 1)
    
    for n in range(low, high + 1):
        n_str = str(n)
        if len(n_str) < total_len:
            continue
        cyclic_val = cyclic(n_str, K)
        if n + cyclic_val == code_N:
            print(n)
            return
            
    print("")

if __name__ == "__main__":
    main()
