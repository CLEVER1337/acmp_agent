
def main():
    with open('INPUT.TXT', 'r') as f:
        code_n = int(f.readline().strip())
        k = int(f.readline().strip())
    
    s = str(code_n)
    n_len = len(s)
    
    for split_point in range(k, n_len):
        left_part = s[:split_point]
        right_part = s[split_point:]
        
        cyclic_part = left_part[-k:]
        remaining_left = left_part[:-k]
        
        try:
            cyclic_num = int(cyclic_part)
            remaining_left_num = int(remaining_left) if remaining_left else 0
            right_num = int(right_part) if right_part else 0
            
            n_candidate = int(remaining_left + right_part)
            cyclic_result = int(cyclic_part + remaining_left)
            
            if n_candidate + cyclic_result == code_n:
                print(n_candidate)
                return
                
        except ValueError:
            continue
    
    print(code_n // 2)

if __name__ == '__main__':
    main()
