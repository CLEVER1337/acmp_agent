
k = int(input().strip())

if k > 240:
    print("NO")
else:
    total_minutes = (k - 1) * 10
    hours = total_minutes // 60
    minutes = total_minutes % 60
    print(f"{hours} {minutes}")
