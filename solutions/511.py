
k = int(input().strip())

if k < 1:
    print("NO")
else:
    total_minutes = 0
    served = 0
    time = 0
    
    while served < k:
        if time % 10 == 0 and time < 5:
            served += 1
        elif time >= 5:
            served += 1
            if time % 10 == 5:
                served += 1
        if served >= k:
            break
        time += 1
    
    end_time = 8 * 60 + time
    if end_time > 20 * 60:
        print("NO")
    else:
        hours = time // 60
        minutes = time % 60
        print(f"{hours} {minutes}")
