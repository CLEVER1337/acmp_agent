
def get_valid_numbers(s):
    n = len(s)
    valid = []
    for i in range(n):
        shifted = s[i:] + s[:i]
        if shifted[0] != '0':
            valid.append(int(shifted))
    return valid

def main():
    with open('INPUT.TXT', 'r') as f:
        s = f.readline().strip()
        t = f.readline().strip()
    
    s_nums = get_valid_numbers(s)
    t_nums = get_valid_numbers(t)
    
    if not s_nums or not t_nums:
        result = 0
    else:
        max_diff = -10**18
        for x in s_nums:
            for y in t_nums:
                diff = x - y
                if diff > max_diff:
                    max_diff = diff
        result = max_diff
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(result))

if __name__ == '__main__':
    main()
