
n = int(input())
answers = list(map(int, input().split()))
total = 0
current_streak = 0

for ans in answers:
    if ans == 1:
        current_streak += 1
        total += current_streak
    else:
        current_streak = 0

print(total)
