
def main():
    K = int(input().strip())
    max_consecutive = 0
    for start_day in range(7):
        holidays = set()
        
        for i in range(K):
            holidays.add(i)
        
        feb_23 = 31 + 22
        mar_8 = 31 + 28 + 7
        
        holidays.add(feb_23)
        holidays.add(mar_8)
        
        weekend = set()
        for day in range(366):
            weekday = (start_day + day) % 7
            if weekday >= 5:
                weekend.add(day)
        
        non_working = holidays | weekend
        
        consecutive = 0
        current_streak = 0
        for day in range(366):
            if day in non_working:
                current_streak += 1
                consecutive = max(consecutive, current_streak)
            else:
                current_streak = 0
        
        max_consecutive = max(max_consecutive, consecutive)
    
    print(max_consecutive)

if __name__ == "__main__":
    main()
