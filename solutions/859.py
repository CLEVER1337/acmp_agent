
n = input().strip()
if n == '0':
    print(0)
else:
    num = int(n)
    if num % 2 == 0:
        result = num // 2 * (num + 1)
    else:
        result = (num + 1) // 2 * num
    print(result)
