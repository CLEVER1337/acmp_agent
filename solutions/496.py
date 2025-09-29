
n = int(input())
a = list(map(int, input().split()))
max_sum = 0
for i in range(n):
    current_sum = a[i] + a[(i-1) % n] + a[(i+1) % n]
    if current_sum > max_sum:
        max_sum = current_sum
print(max_sum)
