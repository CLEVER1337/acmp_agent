
def main():
    import sys
    data = sys.stdin.read().split()
    K = int(data[0])
    p1 = int(data[1]) / 100.0
    p2 = int(data[2]) / 100.0
    p3 = int(data[3]) / 100.0
    
    E_chess_win = p1
    E_chess_draw = p3 * 0.5
    E_volleyball = 1 - p2
    
    E_senior_per_chess = E_chess_win + E_chess_draw
    E_junior_per_chess = (1 - p1 - p3) + E_chess_draw
    
    E_senior_per_volleyball = E_volleyball
    E_junior_per_volleyball = p2
    
    diff_per_chess = abs(E_senior_per_chess - E_junior_per_chess)
    diff_per_volleyball = abs(E_senior_per_volleyball - E_junior_per_volleyball)
    
    if diff_per_chess == 0:
        min_chess = K
    elif diff_per_volleyball == 0:
        min_chess = 0
    else:
        n = int(round(K * diff_per_volleyball / (diff_per_chess + diff_per_volleyball)))
        n = max(0, min(K, n))
        candidates = [n-1, n, n+1]
        best_chess = None
        best_diff = float('inf')
        
        for chess in candidates:
            if 0 <= chess <= K:
                volleyball = K - chess
                total_diff = abs(chess * (E_senior_per_chess - E_junior_per_chess) + 
                               volleyball * (E_senior_per_volleyball - E_junior_per_volleyball))
                if total_diff < best_diff:
                    best_diff = total_diff
                    best_chess = chess
                elif total_diff == best_diff and chess < best_chess:
                    best_chess = chess
        
        min_chess = best_chess
    
    print(min_chess)

if __name__ == "__main__":
    main()
