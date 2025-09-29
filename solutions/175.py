
def main():
    digits = {
        '0': [1, 1, 1, 1, 1, 1, 0],
        '1': [0, 1, 1, 0, 0, 0, 0],
        '2': [1, 1, 0, 1, 1, 0, 1],
        '3': [1, 1, 1, 1, 0, 0, 1],
        '4': [0, 1, 1, 0, 0, 1, 1],
        '5': [1, 0, 1, 1, 0, 1, 1],
        '6': [1, 0, 1, 1, 1, 1, 1],
        '7': [1, 1, 1, 0, 0, 0, 0],
        '8': [1, 1, 1, 1, 1, 1, 1],
        '9': [1, 1, 1, 1, 0, 1, 1]
    }
    
    time_str = input().strip()
    hh, mm = map(int, time_str.split(':'))
    
    def get_display(time_str):
        h, m = time_str.split(':')
        h = h.zfill(2)
        m = m.zfill(2)
        
        display = []
        if h[0] != '0':
            display.append(digits[h[0]])
        else:
            display.append([0]*7)
        display.append(digits[h[1]])
        display.append(digits[m[0]])
        display.append(digits[m[1]])
        return display
    
    def count_active_segments(display):
        return [sum(display[i][j] for i in range(4)) for j in range(7)]
    
    initial_display = get_display(time_str)
    initial_segments = count_active_segments(initial_display)
    
    time_minutes = hh * 60 + mm
    minutes_passed = 0
    
    while True:
        current_time_minutes = (time_minutes + minutes_passed) % (24 * 60)
        current_hh = current_time_minutes // 60
        current_mm = current_time_minutes % 60
        
        time_str = f"{current_hh:02d}:{current_mm:02d}"
        current_display = get_display(time_str)
        current_segments = count_active_segments(current_display)
        
        all_segments_tested = True
        for i in range(7):
            if initial_segments[i] == 0 and current_segments[i] == 0:
                all_segments_tested = False
                break
            if initial_segments[i] == 4 and current_segments[i] == 4:
                all_segments_tested = False
                break
        
        if all_segments_tested:
            break
            
        minutes_passed += 1
        
        if minutes_passed > 24 * 60:
            minutes_passed = 0
            break
    
    print(minutes_passed)

if __name__ == "__main__":
    main()
