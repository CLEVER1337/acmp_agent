
n = int(input().strip())
sectors = list(map(int, input().split()))
a, b, k = map(int, input().split())

max_win = 0

if b == a:
    speeds = [a]
else:
    speeds = [a, b]

for speed in speeds:
    if speed <= k:
        rotations = 0
    else:
        rotations = (speed - 1) // k
    
    clockwise_pos = rotations % n
    counterclockwise_pos = (-rotations) % n
    
    max_win = max(max_win, sectors[clockwise_pos], sectors[counterclockwise_pos])

print(max_win)
