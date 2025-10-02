
def days_in_month(month):
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return months[month - 1]

def date_to_days(date_str):
    day, month, year = map(int, date_str.split('.'))
    days = 0
    
    # Добавляем дни из предыдущих месяцев
    for m in range(1, month):
        days += days_in_month(m)
    
    # Добавляем дни текущего месяца
    days += day
    
    # Добавляем дни за предыдущие годы
    if year == 94:  # 1994 год
        days += 365  # полный 1993 год
    
    return days

with open('INPUT.TXT', 'r') as f:
    petya_date = f.readline().strip()
    vasya_date = f.readline().strip()

petya_days = date_to_days(petya_date)
vasya_days = date_to_days(vasya_date)

result = petya_days - vasya_days

with open('OUTPUT.TXT', 'w') as f:
    f.write(str(result))
