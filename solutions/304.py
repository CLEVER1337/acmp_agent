
def main():
    import sys
    from math import comb
    
    def count_games(a, b):
        if a < b:
            a, b = b, a
        if a < 25:
            return 0
        if a == 25:
            if b >= 24:
                return 0
            return comb(a + b - 1, b)
        if a - b != 2:
            return 0
        return comb(48, 24) * pow(2, b - 24)
    
    def count_tiebreak(a, b):
        if a < b:
            a, b = b, a
        if a < 15:
            return 0
        if a == 15:
            if b >= 14:
                return 0
            return comb(a + b - 1, b)
        if a - b != 2:
            return 0
        return comb(28, 14) * pow(2, b - 14)
    
    data = sys.stdin.read().split()
    n = int(data[0])
    scores = []
    for i in range(1, n + 1):
        score_str = data[i]
        a, b = map(int, score_str.split(':'))
        scores.append((a, b))
    
    total = 1
    for i, (a, b) in enumerate(scores):
        if i == 4:
            total *= count_tiebreak(a, b)
        else:
            total *= count_games(a, b)
    
    print(total)

if __name__ == "__main__":
    main()
