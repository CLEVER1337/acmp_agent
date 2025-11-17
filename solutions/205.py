
import sys

def parse_time(s):
    parts = s.split(':')
    if len(parts) == 1:
        return 0, 0, int(parts[0])
    elif len(parts) == 2:
        return 0, int(parts[0]), int(parts[1])
    else:
        return int(parts[0]), int(parts[1]), int(parts[2])

def normalize(h, m, s):
    total_seconds = h * 3600 + m * 60 + s
    days = total_seconds // 86400
    remaining_seconds = total_seconds % 86400
    h = remaining_seconds // 3600
    remaining_seconds %= 3600
    m = remaining_seconds // 60
    s = remaining_seconds % 60
    return days, h, m, s

def main():
    data = sys.stdin.read().splitlines()
    current_time_str = data[0].strip()
    interval_str = data[1].strip()
    
    hh, mm, ss = map(int, current_time_str.split(':'))
    total_current_seconds = hh * 3600 + mm * 60 + ss
    
    h_int, m_int, s_int = parse_time(interval_str)
    total_interval_seconds = h_int * 3600 + m_int * 60 + s_int
    
    total_final_seconds = total_current_seconds + total_interval_seconds
    days = total_final_seconds // 86400
    remaining_seconds = total_final_seconds % 86400
    
    h = remaining_seconds // 3600
    remaining_seconds %= 3600
    m = remaining_seconds // 60
    s = remaining_seconds % 60
    
    if days > 0:
        print(f"{h:02d}:{m:02d}:{s:02d}+{days} days")
    else:
        print(f"{h:02d}:{m:02d}:{s:02d}")

if __name__ == "__main__":
    main()
