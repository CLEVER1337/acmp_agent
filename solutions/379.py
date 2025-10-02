
def main():
    with open("INPUT.TXT", "r") as f:
        day, month = map(int, f.readline().split())
    
    days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    def is_valid_date(d, m):
        return 1 <= m <= 12 and 1 <= d <= days_in_month[m-1]
    
    memo = {}
    
    def can_win(d, m):
        if (d, m) == (31, 12):
            return False
        
        if (d, m) in memo:
            return memo[(d, m)]
        
        moves = []
        if is_valid_date(d + 1, m):
            moves.append((d + 1, m))
        if is_valid_date(d + 2, m):
            moves.append((d + 2, m))
        if is_valid_date(d, m + 1):
            moves.append((d, m + 1))
        if is_valid_date(d, m + 2):
            moves.append((d, m + 2))
        
        if not moves:
            memo[(d, m)] = False
            return False
        
        for next_d, next_m in moves:
            if not can_win(next_d, next_m):
                memo[(d, m)] = True
                return True
        
        memo[(d, m)] = False
        return False
    
    result = 1 if can_win(day, month) else 2
    
    with open("OUTPUT.TXT", "w") as f:
        f.write(str(result))

if __name__ == "__main__":
    main()
