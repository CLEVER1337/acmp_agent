
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

def days_until_birthday(b_day, b_month, c_day, c_month, c_year):
    if (c_month, c_day) == (b_month, b_day):
        return 0
    
    if (c_month, c_day) < (b_month, b_day):
        days_left = 0
        current_month = c_month
        current_day = c_day
        current_year = c_year
        
        while (current_month, current_day) != (b_month, b_day):
            days_left += 1
            current_day += 1
            if current_day > days_in_month(current_month, current_year):
                current_day = 1
                current_month += 1
                if current_month > 12:
                    current_month = 1
                    current_year += 1
        return days_left
    
    else:
        days_left = 0
        current_month = c_month
        current_day = c_day
        current_year = c_year
        
        while (current_month, current_day) != (b_month, b_day):
            days_left += 1
            current_day += 1
            if current_day > days_in_month(current_month, current_year):
                current_day = 1
                current_month += 1
                if current_month > 12:
                    current_month = 1
                    current_year += 1
        return days_left

with open('INPUT.TXT', 'r') as f:
    b_data = f.readline().split()
    c_data = f.readline().split()
    
b_day = int(b_data[0])
b_month = int(b_data[1])
c_day = int(c_data[0])
c_month = int(c_data[1])
c_year = int(c_data[2])

result = days_until_birthday(b_day, b_month, c_day, c_month, c_year)

with open('OUTPUT.TXT', 'w') as f:
    f.write(str(result))
