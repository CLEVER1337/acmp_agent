
def main():
    days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day, month = map(int, input().split())
    month -= 1
    
    n = 12
    m = 31
    dp = [[False] * (m + 1) for _ in range(n + 1)]
    
    dp[11][30] = True
    
    for mm in range(11, -1, -1):
        max_day = days_in_month[mm] - 1 if mm == 11 else days_in_month[mm]
        for dd in range(max_day, -1, -1):
            if mm == 11 and dd == 30:
                continue
                
            moves = []
            if dd + 1 < days_in_month[mm]:
                moves.append((mm, dd + 1))
            if dd + 2 < days_in_month[mm]:
                moves.append((mm, dd + 2))
            if mm + 1 < 12:
                new_days = min(days_in_month[mm + 1], dd)
                if new_days > 0:
                    moves.append((mm + 1, new_days - 1))
            if mm + 2 < 12:
                new_days = min(days_in_month[mm + 2], dd)
                if new_days > 0:
                    moves.append((mm + 2, new_days - 1))
                    
            winning = False
            for nm, nd in moves:
                if nm == 11 and nd == 30:
                    winning = True
                    break
                if not dp[nm][nd]:
                    winning = True
                    break
                    
            dp[mm][dd] = winning
            
    print(1 if dp[month][day] else 2)

if __name__ == "__main__":
    main()
