
def is_leap(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

def days_in_month(month, year):
    if month == 2:
        return 29 if is_leap(year) else 28
    if month in [4, 6, 9, 11]:
        return 30
    return 31

def date_to_days(d, m, y):
    total = 0
    for year in range(1, y):
        total += 366 if is_leap(year) else 365
    for month in range(1, m):
        total += days_in_month(month, y)
    total += d
    return total

def main():
    with open('INPUT.TXT', 'r') as f:
        start_date = f.readline().strip()
        end_date = f.readline().strip()
    
    d1, m1, y1 = map(int, start_date.split('.'))
    d2, m2, y2 = map(int, end_date.split('.'))
    
    days1 = date_to_days(d1, m1, y1)
    days2 = date_to_days(d2, m2, y2)
    
    result = days2 - days1
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(result))

if __name__ == '__main__':
    main()
