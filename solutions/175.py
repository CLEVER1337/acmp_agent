
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

def get_display_state(time_str):
    hh, mm = time_str.split(':')
    h1 = '0' if hh[0] == '0' else hh[0]
    h2 = hh[1]
    m1 = mm[0]
    m2 = mm[1]
    
    states = []
    if h1 != '0':
        states.append(digits[h1])
    states.append(digits[h2])
    states.append(digits[m1])
    states.append(digits[m2])
    
    return states

def count_active_segments(states):
    total_segments = [0] * 7
    for state in states:
        for i in range(7):
            total_segments[i] += state[i]
    return total_segments

def is_valid_display(states):
    active_segments = count_active_segments(states)
    return all(0 < count < len(states) for count in active_segments)

def main():
    start_time = input().strip()
    hh, mm = map(int, start_time.split(':'))
    
    time = hh * 60 + mm
    minutes_passed = 0
    
    while True:
        current_time = (time + minutes_passed) % (24 * 60)
        hours = current_time // 60
        minutes = current_time % 60
        
        time_str = f"{hours:02d}:{minutes:02d}"
        display_states = get_display_state(time_str)
        
        if is_valid_display(display_states):
            break
            
        minutes_passed += 1
        
    print(minutes_passed)

if __name__ == "__main__":
    main()
