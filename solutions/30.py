
def count_digits_in_time(start, end):
    def time_to_seconds(time_str):
        h, m, s = map(int, time_str.split(':'))
        return h * 3600 + m * 60 + s
    
    def get_time_digits(seconds):
        total_seconds = seconds
        s = total_seconds % 60
        total_seconds //= 60
        m = total_seconds % 60
        h = total_seconds // 60
        return f"{h:02d}{m:02d}{s:02d}"
    
    start_seconds = time_to_seconds(start)
    end_seconds = time_to_seconds(end)
    
    digit_count = [0] * 10
    
    for seconds in range(start_seconds, end_seconds + 1):
        time_str = get_time_digits(seconds)
        for digit_char in time_str:
            digit = int(digit_char)
            digit_count[digit] += 1
    
    return digit_count

def main():
    with open('INPUT.TXT', 'r') as f:
        start_time = f.readline().strip()
        end_time = f.readline().strip()
    
    result = count_digits_in_time(start_time, end_time)
    
    with open('OUTPUT.TXT', 'w') as f:
        for i in range(10):
            f.write(f"{result[i]}\n")

if __name__ == "__main__":
    main()
