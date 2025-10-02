
n, m, k = map(int, input().split())

if k == 1:
    print(n * m)
else:
    total_icons = 0
    max_white = k - 1
    
    for x in range(1, m + 1):
        red_needed = x // k
        remaining = x % k
        
        if remaining > max_white:
            icons_needed = red_needed + 1 + max_white
        else:
            icons_needed = red_needed + remaining
        
        total_icons += icons_needed
    
    print(total_icons * n)
