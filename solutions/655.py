
def main():
    with open("INPUT.TXT", "r") as f:
        code_n = int(f.readline().strip())
        K = int(f.readline().strip())
    
    s = str(code_n)
    n_len = len(s) - K
    
    for split_pos in range(max(1, n_len), len(s)):
        a = s[:split_pos]
        b = s[split_pos:]
        
        if len(b) != K:
            continue
            
        cyclic_num = int(b + a)
        n_candidate = code_n - cyclic_num
        
        if n_candidate <= 0:
            continue
            
        n_str = str(n_candidate)
        if len(n_str) != n_len:
            continue
            
        expected_cyclic = n_str[-K:] + n_str[:-K]
        if int(expected_cyclic) == cyclic_num:
            print(n_candidate)
            return
            
    print(code_n // 2)

if __name__ == "__main__":
    main()
