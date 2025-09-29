
n = int(input())
a = list(map(int, input().split()))

if n <= 1:
    print(n)
else:
    max_len = 1
    current_len = 1
    prev_sign = 0
    
    for i in range(1, n):
        if a[i] == a[i-1]:
            current_len = 1
            prev_sign = 0
        else:
            curr_sign = 1 if a[i] > a[i-1] else -1
            if prev_sign == 0 or prev_sign != curr_sign:
                current_len += 1
                max_len = max(max_len, current_len)
                prev_sign = curr_sign
            else:
                current_len = 2
                prev_sign = curr_sign
                
    print(max_len)
