
n = int(input())
scores = list(map(int, input().split()))

best_place = 0

for i in range(n):
    if scores[i] % 10 == 5:
        if i < n - 1 and scores[i + 1] < scores[i]:
            has_winner_before = False
            for j in range(i):
                if scores[j] > scores[i]:
                    has_winner_before = True
                    break
            
            if has_winner_before:
                count_better = 0
                for j in range(n):
                    if scores[j] > scores[i]:
                        count_better += 1
                
                place = count_better + 1
                if best_place == 0 or place < best_place:
                    best_place = place

print(best_place)
