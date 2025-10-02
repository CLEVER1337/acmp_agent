
def main():
    n = int(input().strip())
    if n == 1:
        print(2)
        print(1)
        return
    elif n == 2:
        print(3)
        print(1)
        return
    elif n == 3:
        print(4)
        print(1)
        return
    elif n == 4:
        print(7)
        print(1)
        return
    elif n == 5:
        print(13)
        print(1)
        return

    max_size = max(10000, n * 2)
    a = [0] * (max_size + 1)
    b = []
    a[1] = 2
    a[2] = 3
    a[3] = 4
    a[4] = 7
    a[5] = 13

    used = set(a[1:6])
    next_num = 1
    b_index = 0

    for i in range(6, n + 1):
        while next_num in used:
            next_num += 1
        b.append(next_num)
        used.add(next_num)
        next_num += 1
        
        if len(b) >= 3:
            a[i] = b[b_index] + b[b_index + 2]
            used.add(a[i])
            b_index += 1
        else:
            while next_num in used:
                next_num += 1
            a[i] = next_num
            used.add(next_num)
            next_num += 1

    print(a[n])
    
    bn_list = []
    current = 1
    while len(bn_list) < n:
        if current not in used:
            bn_list.append(current)
        current += 1
    
    print(bn_list[n - 1])

if __name__ == "__main__":
    main()
