
def count_games(a, b, is_fifth):
    total = a + b
    if is_fifth:
        win_score = 15
    else:
        win_score = 25
        
    if max(a, b) < win_score:
        return 0
        
    if abs(a - b) < 2:
        return 0
        
    if a < win_score - 1 and b < win_score - 1:
        return 0
        
    if is_fifth:
        if a == win_score - 1 and b >= win_score:
            return 0
        if b == win_score - 1 and a >= win_score:
            return 0
    else:
        if a == win_score - 1 and b >= win_score:
            return 0
        if b == win_score - 1 and a >= win_score:
            return 0
            
    n = a + b
    if a == b + 2:
        if a == win_score:
            return comb(n - 1, win_score - 1)
        else:
            return comb(n - 1, win_score - 1) * pow(2, a - win_score)
    elif a > b:
        if b == win_score - 1:
            return comb(n - 1, b)
        else:
            return comb(n - 1, win_score - 1) * pow(2, a - win_score)
    else:
        if a == win_score - 1:
            return comb(n - 1, a)
        else:
            return comb(n - 1, win_score - 1) * pow(2, b - win_score)

def comb(n, k):
    if k < 0 or k > n:
        return 0
    res = 1
    for i in range(1, k + 1):
        res = res * (n - k + i) // i
    return res

def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    scores = []
    index = 1
    for i in range(n):
        score_str = data[index]
        index += 1
        a, b = map(int, score_str.split(':'))
        scores.append((a, b))
    
    result = 1
    for i, (a, b) in enumerate(scores):
        is_fifth = (i == 4)
        result *= count_games(a, b, is_fifth)
    
    print(result)

if __name__ == '__main__':
    main()
