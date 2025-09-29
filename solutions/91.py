
def main():
    n = int(input().strip())
    a = [0] * (n + 3)
    b = []
    a[1] = 2
    a[2] = 3
    a[3] = 4
    a[4] = 7
    a[5] = 13
    
    if n <= 5:
        print(a[n])
        if n >= 1:
            b_list = [1, 5, 6, 8, 9, 10]
            print(b_list[n - 1] if n <= len(b_list) else '')
        return
    
    max_num = 20000
    used = [False] * (max_num + 1)
    for i in range(1, 6):
        used[a[i]] = True
    
    next_b = 1
    for i in range(6, n + 1):
        while used[next_b]:
            next_b += 1
        b_val = next_b
        b.append(b_val)
        used[b_val] = True
        
        a[i] = b[i - 4 - 1] + b[i - 2 - 1]
        if a[i] <= max_num:
            used[a[i]] = True
    
    print(a[n])
    
    b_set = set()
    for i in range(1, n + 1):
        b_set.add(a[i])
    
    bn_list = []
    num = 1
    while len(bn_list) < n:
        if num not in b_set:
            bn_list.append(num)
        num += 1
    
    print(bn_list[n - 1])

if __name__ == "__main__":
    main()
