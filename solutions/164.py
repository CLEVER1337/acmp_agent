
def digital_root(n_str):
    n = sum(int(d) for d in n_str)
    while n >= 10:
        n = sum(int(d) for d in str(n))
    return n

def main():
    with open('INPUT.TXT', 'r') as f:
        s = f.readline().strip()
    
    n = len(s)
    found = False
    
    for i in range(1, n):
        left_num = s[:i]
        right_num = s[i:]
        
        if left_num and right_num:
            left_root = digital_root(left_num)
            right_root = digital_root(right_num)
            
            if left_root == right_root:
                found = True
                break
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write('YES' if found else 'NO')

if __name__ == '__main__':
    main()
