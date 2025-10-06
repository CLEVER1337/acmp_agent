
def main():
    with open("INPUT.TXT", "r") as f:
        current_time = f.readline().strip()
        interval = f.readline().strip()
    
    hh, mm, ss = map(int, current_time.split(':'))
    total_current_seconds = hh * 3600 + mm * 60 + ss
    
    parts = interval.split(':')
    if len(parts) == 1:
        hours, minutes, seconds = 0, 0, int(parts[0])
    elif len(parts) == 2:
        hours, minutes, seconds = 0, int(parts[0]), int(parts[1])
    else:
        hours, minutes, seconds = int(parts[0]), int(parts[1]), int(parts[2])
    
    total_interval_seconds = hours * 3600 + minutes * 60 + seconds
    
    total_result_seconds = total_current_seconds + total_interval_seconds
    seconds_in_day = 24 * 3600
    
    days = total_result_seconds // seconds_in_day
    remaining_seconds = total_result_seconds % seconds_in_day
    
    result_hh = remaining_seconds // 3600
    remaining_seconds %= 3600
    result_mm = remaining_seconds // 60
    result_ss = remaining_seconds % 60
    
    with open("OUTPUT.TXT", "w") as f:
        f.write(f"{result_hh:02d}:{result_mm:02d}:{result_ss:02d}")
        if days > 0:
            f.write(f"+{days} days")

if __name__ == "__main__":
    main()
