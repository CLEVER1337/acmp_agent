
n = int(input())
arr = list(map(int, input().split()))

max_wait = 0
last_occurrence = {}

for i, route in enumerate(arr):
    if route in last_occurrence:
        distance = i - last_occurrence[route] - 1
        if distance > max_wait:
            max_wait = distance
    last_occurrence[route] = i

print(max_wait)
