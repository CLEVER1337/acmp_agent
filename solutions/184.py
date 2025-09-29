
def main():
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    def to_minutes(date_str):
        parts = date_str.split()
        date_part = parts[0]
        time_part = parts[1]
        
        day, month = map(int, date_part.split('.'))
        hour, minute = map(int, time_part.split(':'))
        
        total_days = sum(months[:month-1]) + day - 1
        return total_days * 24 * 60 + hour * 60 + minute
    
    k = int(input().strip())
    events = []
    for _ in range(k):
        line = input().strip()
        events.append(to_minutes(line))
    
    events.sort()
    
    total_work_minutes = 0
    for i in range(0, len(events), 2):
        start = events[i]
        end = events[i+1]
        
        work_start = 10 * 60
        work_end = 18 * 60
        
        current_day = start // (24 * 60)
        current_minute = start % (24 * 60)
        
        day_end = current_day * 24 * 60 + work_end
        if current_minute < work_start:
            current_minute = work_start
        elif current_minute > work_end:
            current_day += 1
            current_minute = work_start
        
        while current_day * 24 * 60 + current_minute < end:
            day_start = current_day * 24 * 60 + work_start
            day_end = current_day * 24 * 60 + work_end
            
            effective_start = max(current_day * 24 * 60 + current_minute, day_start)
            effective_end = min(end, day_end)
            
            if effective_start < effective_end:
                total_work_minutes += effective_end - effective_start
            
            current_day += 1
            current_minute = work_start
    
    hours = total_work_minutes // 60
    minutes = total_work_minutes % 60
    print(f"{hours}:{minutes:02d}")

if __name__ == "__main__":
    main()
