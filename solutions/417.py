
def main():
    with open('INPUT.TXT', 'r') as f:
        K = int(f.read().strip())
    
    days_of_week = ['Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'Monday']
    months = [
        (31, 'January'), (29, 'February'), (31, 'March'), (30, 'April'), 
        (31, 'May'), (30, 'June'), (31, 'July'), (31, 'August'), 
        (30, 'September'), (31, 'October'), (30, 'November'), (31, 'December')
    ]
    
    total_days = K
    day_of_week = days_of_week[total_days % 7]
    
    day = 1
    month_index = 0
    
    while total_days >= months[month_index][0]:
        total_days -= months[month_index][0]
        month_index += 1
        day = 1
    
    day += total_days
    month = months[month_index][1]
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(f"{day_of_week}, {day} {month}")

if __name__ == "__main__":
    main()
