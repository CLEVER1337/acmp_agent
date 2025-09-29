
def main():
    with open('INPUT.TXT', 'r') as f:
        day, month = map(int, f.readline().split())
    
    # Количество дней в каждом месяце 2008 года (високосный)
    days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Преобразуем дату в количество дней от начала года
    total_days = 0
    for i in range(month - 1):
        total_days += days_in_month[i]
    total_days += day
    
    # Рассчитываем расстояние до конца года (31 декабря)
    distance = 365 - total_days
    
    # Используем теорию игр: если расстояние до конца кратно 3, то проигрышная позиция
    if distance % 3 == 0:
        result = 2
    else:
        result = 1
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(result))

if __name__ == '__main__':
    main()
