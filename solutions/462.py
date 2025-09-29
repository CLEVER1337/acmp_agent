
n = int(input())
count = n - (n // 2 + n // 3 + n // 5 - n // 6 - n // 10 - n // 15 + n // 30)
print(count)
