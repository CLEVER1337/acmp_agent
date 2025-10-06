
n = int(input().strip())
houses = list(map(int, input().split()))
print(houses[(n - 1) // 2])
