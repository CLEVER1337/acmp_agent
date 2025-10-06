
def main():
    import sys
    data = sys.stdin.read().splitlines()
    k = int(data[0])
    dates = data[1:1+k]
    
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    def parse_date(s):
        parts = s.split()
        date_part = parts[0]
        time_part = parts[1]
        day, month = map(int, date_part[:-1].split('.'))
        hour, minute = map(int, time_part.split(':'))
        return month, day, hour, minute
    
    def to_minutes(month, day, hour, minute):
        total_minutes = 0
        for i in range(month - 1):
            total_minutes += months[i] * 24 * 60
        total_minutes += (day - 1) * 24 * 60
        total_minutes += hour * 60
        total_minutes += minute
        return total_minutes
    
    events = []
    for date_str in dates:
        month, day, hour, minute = parse_date(date_str)
        events.append(to_minutes(month, day, hour, minute))
    
    events.sort()
    
    total_work_minutes = 0
    for i in range(0, len(events), 2):
        start = events[i]
        end = events[i+1]
        
        work_start = 10 * 60
        work_end = 18 * 60
        
        current = start
        while current < end:
            day_start = (current // (24 * 60)) * (24 * 60)
            day_minute = current % (24 * 60)
            
            work_start_abs = day_start + work_start
            work_end_abs = day_start + work_end
            
            if day_minute < work_start:
                current = work_start_abs
                continue
                
            if day_minute >= work_end:
                current = day_start + 24 * 60
                continue
                
            segment_end = min(end, work_end_abs)
            if current < segment_end:
                total_work_minutes += segment_end - current
                current = segment_end
            else:
                current = day_start + 24 * 60
    
    hours = total_work_minutes // 60
    minutes = total_work_minutes % 60
    
    print(f"{hours}:{minutes:02d}")

if __name__ == "__main__":
    main()
