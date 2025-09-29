
n = int(input().strip())

if n == 0:
    print("0 0")
else:
    min_second = (n + 5) // 6
    max_second = n * 6
    
    if n % 6 != 0:
        min_second = (n // 6) + 1
    else:
        min_second = n // 6
        
    print(f"{min_second} {max_second}")
