
k = int(input())
if k < 1:
    print("NO")
else:
    total_time = (k - 1) * 10
    if total_time >= 720:
        print("NO")
    else:
        hours = total_time // 60
        minutes = total_time % 60
        print(f"{hours} {minutes}")
