
def main():
    k = int(input().strip())
    
    days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month_names = ["January", "February", "March", "April", "May", "June", 
                  "July", "August", "September", "October", "November", "December"]
    weekdays = ["Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "Monday"]
    
    total_days = k
    weekday_index = total_days % 7
    weekday = weekdays[weekday_index]
    
    day_count = total_days
    month = 0
    day = 0
    
    for i in range(12):
        if day_count < days_in_month[i]:
            month = i
            day = day_count + 1
            break
        day_count -= days_in_month[i]
    
    month_name = month_names[month]
    
    with open("OUTPUT.TXT", "w") as f:
        f.write(f"{weekday}, {day} {month_name}")

if __name__ == "__main__":
    main()
