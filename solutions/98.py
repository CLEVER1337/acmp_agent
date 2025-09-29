
n = int(input())
arr = list(map(int, input().split()))

left = 0
right = n - 1
first_score = 0
second_score = 0
turn = 0  # 0 - первый игрок, 1 - второй

while left <= right:
    if arr[left] >= arr[right]:
        num = arr[left]
        left += 1
    else:
        num = arr[right]
        right -= 1
        
    if turn == 0:
        first_score += num
    else:
        second_score += num
        
    turn = 1 - turn

print(f"{first_score}:{second_score}")
