
n = int(input())
arr = list(map(int, input().split()))

target = list(range(1, n + 1))
current_positions = {val: idx for idx, val in enumerate(arr)}

max_chain = 0
for num in range(1, n + 1):
    chain = 1
    next_num = num + 1
    while next_num <= n and current_positions[next_num] > current_positions[num]:
        chain += 1
        num = next_num
        next_num += 1
    max_chain = max(max_chain, chain)

result = n - max_chain
print(result)
