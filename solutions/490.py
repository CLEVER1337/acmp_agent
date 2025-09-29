
def days_since_1993(date_str):
    day, month, year = map(int, date_str.split('.'))
    full_year = 1993 if year == 93 else 1994
    
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    total_days = 0
    if full_year == 1994:
        total_days += 365
    
    for m in range(month - 1):
        total_days += days_in_month[m]
    
    total_days += day - 1
    return total_days

with open('INPUT.TXT', 'r') as f:
    petya_date = f.readline().strip()
    vasya_date = f.readline().strip()

petya_days = days_since_1993(petya_date)
vasya_days = days_since_1993(vasya_date)

difference = petya_days - vasya_days

with open('OUTPUT.TXT', 'w') as f:
    f.write(str(difference))
