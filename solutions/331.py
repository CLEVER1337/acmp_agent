
def main():
    with open('INPUT.TXT', 'r') as f:
        departure = f.readline().strip()
        travel_time = f.readline().strip()
    
    hours_dep, minutes_dep = map(int, departure.split(':'))
    hours_travel, minutes_travel = map(int, travel_time.split())
    
    total_minutes = hours_dep * 60 + minutes_dep + hours_travel * 60 + minutes_travel
    
    days = total_minutes // (24 * 60)
    remaining_minutes = total_minutes % (24 * 60)
    
    hours_arr = remaining_minutes // 60
    minutes_arr = remaining_minutes % 60
    
    result = f"{hours_arr:02d}:{minutes_arr:02d}"
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(result)

if __name__ == "__main__":
    main()
