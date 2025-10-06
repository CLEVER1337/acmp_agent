
def main():
    s = input().strip()
    t = input().strip()
    
    def get_valid_shifts(string):
        n = len(string)
        shifts = []
        for i in range(n):
            shift = string[i:] + string[:i]
            if shift[0] != '0':
                shifts.append(shift)
        return shifts
    
    s_shifts = get_valid_shifts(s)
    t_shifts = get_valid_shifts(t)
    
    if not s_shifts:
        s_shifts = [s]
    if not t_shifts:
        t_shifts = [t]
    
    s_nums = [int(x) for x in s_shifts]
    t_nums = [int(x) for x in t_shifts]
    
    max_diff = -10**18
    for x in s_nums:
        for y in t_nums:
            diff = x - y
            if diff > max_diff:
                max_diff = diff
                
    print(str(max_diff))

if __name__ == "__main__":
    main()
