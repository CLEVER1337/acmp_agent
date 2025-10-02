
def is_palindrome(time_str):
    return time_str == time_str[::-1]

def main():
    with open('INPUT.TXT', 'r') as f:
        time_input = f.readline().strip()
    
    hh, mm = map(int, time_input.split(':'))
    current_minutes = hh * 60 + mm
    
    for delta in range(0, 1440):
        total_minutes = (current_minutes + delta) % 1440
        h = total_minutes // 60
        m = total_minutes % 60
        
        time_str = f"{h:02d}:{m:02d}"
        if is_palindrome(time_str.replace(':', '')):
            with open('OUTPUT.TXT', 'w') as f:
                f.write(time_str)
            return

if __name__ == "__main__":
    main()
