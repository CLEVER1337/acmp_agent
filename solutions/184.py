
def parse_date(s):
    parts = s.split()
    date_part = parts[0]
    time_part = parts[1]
    
    day_month = date_part.split('.')
    day = int(day_month[0])
    month = int(day_month[1])
    
    hour_minute = time_part.split(':')
    hour = int(hour_minute[0])
    minute = int(hour_minute[1])
    
    return month, day, hour, minute

def date_to_minutes(month, day, hour, minute):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total_minutes = 0
    
    for m in range(1, month):
        total_minutes += days_in_month[m-1] * 24 * 60
    
    total_minutes += (day - 1) * 24 * 60
    total_minutes += hour * 60
    total_minutes += minute
    
    return total_minutes

def is_work_time(hour, minute):
    time_minutes = hour * 60 + minute
    return 10 * 60 <= time_minutes <= 18 * 60

def get_work_minutes_in_day(start_minutes, end_minutes):
    day_start = 10 * 60
    day_end = 18 * 60
    
    start_minutes = max(start_minutes, day_start)
    end_minutes = min(end_minutes, day_end)
    
    return max(0, end_minutes - start_minutes)

def calculate_work_time(start_date, end_date):
    start_month, start_day, start_hour, start_minute = parse_date(start_date)
    end_month, end_day, end_hour, end_minute = parse_date(end_date)
    
    start_total_minutes = date_to_minutes(start_month, start_day, start_hour, start_minute)
    end_total_minutes = date_to_minutes(end_month, end_day, end_hour, end_minute)
    
    if start_total_minutes > end_total_minutes:
        return 0
    
    if start_month == end_month and start_day == end_day:
        if is_work_time(start_hour, start_minute) and is_work_time(end_hour, end_minute):
            return end_total_minutes - start_total_minutes
        else:
            return get_work_minutes_in_day(start_total_minutes % (24*60), end_total_minutes % (24*60))
    
    total_work_minutes = 0
    
    current_month = start_month
    current_day = start_day
    
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    while current_month != end_month or current_day != end_day:
        day_start_minutes = date_to_minutes(current_month, current_day, 10, 0)
        day_end_minutes = date_to_minutes(current_month, current_day, 18, 0)
        
        if current_month == start_month and current_day == start_day:
            if is_work_time(start_hour, start_minute):
                work_start = date_to_minutes(current_month, current_day, start_hour, start_minute)
                total_work_minutes += day_end_minutes - work_start
        else:
            total_work_minutes += 8 * 60
        
        current_day += 1
        if current_day > days_in_month[current_month-1]:
            current_day = 1
            current_month += 1
    
    if is_work_time(end_hour, end_minute):
        work_end = date_to_minutes(end_month, end_day, end_hour, end_minute)
        day_start_minutes = date_to_minutes(end_month, end_day, 10, 0)
        total_work_minutes += work_end - day_start_minutes
    
    return total_work_minutes

def main():
    with open('INPUT.TXT', 'r') as f:
        k = int(f.readline().strip())
        dates = []
        for _ in range(k):
            line = f.readline().strip()
            date_str = line[:5] + '.' + line[6:]
            dates.append(date_str)
    
    starts = []
    ends = []
    
    for i in range(0, len(dates), 2):
        starts.append(dates[i])
        ends.append(dates[i+1])
    
    total_work_minutes = 0
    for start, end in zip(starts, ends):
        total_work_minutes += calculate_work_time(start, end)
    
    hours = total_work_minutes // 60
    minutes = total_work_minutes % 60
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(f"{hours}:{minutes:02d}")

if __name__ == "__main__":
    main()
