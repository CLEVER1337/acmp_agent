
n, m, d, k = map(int, input().split())
total_area = n * m * d * d + (n + m) * d * (k - m * d) - n * m * d * d
print(total_area)
