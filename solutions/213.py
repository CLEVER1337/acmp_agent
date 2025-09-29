
def main():
    with open('INPUT.TXT', 'r') as f:
        n = int(f.readline().strip())
        test_scores = list(map(int, f.readline().split()))
        bonus = int(f.readline().strip())
        m = int(f.readline().strip())
        
        attempts = []
        for _ in range(m):
            attempt = list(map(int, f.readline().split()))
            attempts.append(attempt)
    
    total_max_score = sum(test_scores) + bonus
    results = []
    best_result = 0
    
    for i in range(m):
        current_score = 0
        all_passed = True
        
        for j in range(n):
            if attempts[i][j] == 1:
                current_score += test_scores[j]
            else:
                all_passed = False
        
        if all_passed:
            current_score += bonus
        
        penalty = 2 * i
        current_score_with_penalty = max(0, current_score - penalty)
        
        if current_score_with_penalty > best_result:
            best_result = current_score_with_penalty
        
        results.append(best_result)
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(' '.join(map(str, results)))

if __name__ == '__main__':
    main()
