
n = int(input())
heights = list(map(int, input().split()))

heights.sort()
if n % 2 == 1:
    median = heights[n // 2]
else:
    median = (heights[n // 2 - 1] + heights[n // 2]) / 2

print("{:.10f}".format(median))
