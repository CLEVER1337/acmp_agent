
def main():
    K = int(input().strip())
    max_consecutive = 0
    for start_day in range(7):
        holidays = set()
        for i in range(K):
            holidays.add(i + 1)
        holidays.add(23 + 31)
        holidays.add(23 + 31 + 28)
        day = 1
        calendar = []
        for i in range(365):
            weekday = (start_day + i) % 7
            is_weekend = weekday >= 5
            is_holiday = (i + 1) in holidays
            calendar.append((is_holiday or is_weekend, is_holiday, is_weekend))
        transferred = [False] * 365
        for i in range(365):
            if calendar[i][1] and calendar[i][2]:
                j = i + 1
                while j < 365 and (calendar[j][0] or transferred[j]):
                    j += 1
                if j < 365:
                    transferred[j] = True
        non_working = [False] * 365
        for i in range(365):
            non_working[i] = calendar[i][0] or transferred[i]
        current = 0
        for i in range(365):
            if non_working[i]:
                current += 1
            else:
                if current > max_consecutive:
                    max_consecutive = current
                current = 0
        if current > max_consecutive:
            max_consecutive = current
    print(max_consecutive)

if __name__ == '__main__':
    main()
