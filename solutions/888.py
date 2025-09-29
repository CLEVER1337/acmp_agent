
n = int(input())
answers = list(map(int, input().split()))

total_score = 0
current_streak = 0

for answer in answers:
    if answer == 1:
        current_streak += 1
        total_score += current_streak
    else:
        current_streak = 0

print(total_score)
