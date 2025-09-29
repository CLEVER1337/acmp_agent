
n = int(input())
arr = list(map(int, input().split()))

last_occurrence = {}
max_wait = 0

for i, route in enumerate(arr):
    if route in last_occurrence:
        wait = i - last_occurrence[route] - 1
        if wait > max_wait:
            max_wait = wait
    last_occurrence[route] = i

print(max_wait)
