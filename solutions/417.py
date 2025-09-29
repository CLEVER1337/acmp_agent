
def main():
    with open('INPUT.TXT', 'r') as f:
        K = int(f.read().strip())
    
    days_of_week = ['Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'Monday']
    months = [
        ('January', 31),
        ('February', 29),  # 2008 год - високосный
        ('March', 31),
        ('April', 30),
        ('May', 31),
        ('June', 30),
        ('July', 31),
        ('August', 31),
        ('September', 30),
        ('October', 31),
        ('November', 30),
        ('December', 31)
    ]
    
    day_of_week = days_of_week[K % 7]
    
    day_count = K
    month_index = 0
    day_number = 1
    
    for month_name, days_in_month in months:
        if day_count < days_in_month:
            day_number += day_count
            break
        day_count -= days_in_month
        month_index += 1
        day_number = 1
    
    month_name = months[month_index][0]
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(f"{day_of_week}, {day_number} {month_name}")

if __name__ == '__main__':
    main()
