
def get_max_number(s):
    n = len(s)
    shifts = [s[i:] + s[:i] for i in range(n)]
    valid_numbers = []
    for shift in shifts:
        if shift[0] != '0':
            valid_numbers.append(int(shift))
    if not valid_numbers:
        return None
    return max(valid_numbers)

def main():
    with open('INPUT.TXT', 'r') as f:
        s = f.readline().strip()
        t = f.readline().strip()
    
    s_shifts = []
    n = len(s)
    for i in range(n):
        candidate = s[i:] + s[:i]
        if candidate[0] != '0':
            s_shifts.append(int(candidate))
    
    t_shifts = []
    m = len(t)
    for i in range(m):
        candidate = t[i:] + t[:i]
        if candidate[0] != '0':
            t_shifts.append(int(candidate))
    
    if not s_shifts or not t_shifts:
        return
    
    max_diff = -10**18
    for x in s_shifts:
        for y in t_shifts:
            diff = x - y
            if diff > max_diff:
                max_diff = diff
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(max_diff))

if __name__ == '__main__':
    main()
