
def is_palindrome(time_str):
    return time_str == time_str[::-1]

def main():
    with open("INPUT.TXT", "r") as f:
        start_time = f.readline().strip()
    
    hh, mm = map(int, start_time.split(':'))
    
    current_minutes = hh * 60 + mm
    
    for delta in range(24 * 60):
        total_minutes = (current_minutes + delta) % (24 * 60)
        test_hh = total_minutes // 60
        test_mm = total_minutes % 60
        
        time_str = f"{test_hh:02d}:{test_mm:02d}"
        if is_palindrome(time_str.replace(':', '')):
            with open("OUTPUT.TXT", "w") as f:
                f.write(time_str)
            return

if __name__ == "__main__":
    main()
