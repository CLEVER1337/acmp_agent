
n = int(input().strip())

if n <= 0:
    print("0 0")
else:
    min_second = (n + 5) // 6 * 2
    max_second = (n + 1) // 2 * 7
    
    if n % 2 == 1:
        min_second = max(min_second, 7)
        max_second = max_second - 1
    
    print(f"{min_second} {max_second}")
