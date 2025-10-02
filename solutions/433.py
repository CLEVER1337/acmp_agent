
n = int(input())
s = input().strip()

prefix_sum = [0]
for char in s:
    prefix_sum.append(prefix_sum[-1] + (1 if char == 'a' else -1))

count = {}
for val in prefix_sum:
    count[val] = count.get(val, 0) + 1

result = 0
for val in count:
    k = count[val]
    result += k * (k - 1) // 2

print(result)
