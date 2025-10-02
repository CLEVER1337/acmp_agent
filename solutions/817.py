
n, m, d, k = map(int, input().split())
total_area = n * k * d + m * k * d - n * m * d * d
print(total_area)
