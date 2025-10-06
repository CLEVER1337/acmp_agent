
n = int(input())
arr = list(map(int, input().split()))
target = list(range(1, n+1))
positions = {val: idx for idx, val in enumerate(target)}
max_seq = 0
current_seq = 0
prev_pos = -1

for num in arr:
    pos = positions[num]
    if pos == prev_pos + 1:
        current_seq += 1
        prev_pos = pos
    else:
        if current_seq > max_seq:
            max_seq = current_seq
        current_seq = 1
        prev_pos = pos

if current_seq > max_seq:
    max_seq = current_seq

print(n - max_seq)
