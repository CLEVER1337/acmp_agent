
n = int(input())
a = list(map(int, input().split()))

stack = []
count = 0

for val in a:
    while stack and stack[-1] > val:
        stack.pop()
    if stack and stack[-1] == val:
        continue
    if val != 0:
        stack.append(val)
        count += 1

print(count)
