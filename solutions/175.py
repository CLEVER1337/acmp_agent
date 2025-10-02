
def get_digits(n):
    return [n // 10, n % 10]

def get_segments(digit, is_hour=False):
    segments = {
        0: [1, 1, 1, 1, 1, 1, 0],
        1: [0, 1, 1, 0, 0, 0, 0],
        2: [1, 1, 0, 1, 1, 0, 1],
        3: [1, 1, 1, 1, 0, 0, 1],
        4: [0, 1, 1, 0, 0, 1, 1],
        5: [1, 0, 1, 1, 0, 1, 1],
        6: [1, 0, 1, 1, 1, 1, 1],
        7: [1, 1, 1, 0, 0, 0, 0],
        8: [1, 1, 1, 1, 1, 1, 1],
        9: [1, 1, 1, 1, 0, 1, 1]
    }
    if is_hour and digit == 0:
        return [0, 0, 0, 0, 0, 0, 0]
    return segments[digit]

def get_state(time_str):
    hh, mm = map(int, time_str.split(':'))
    h1, h2 = get_digits(hh)
    m1, m2 = get_digits(mm)
    
    state = []
    state.extend(get_segments(h1, True))
    state.extend(get_segments(h2))
    state.extend(get_segments(m1))
    state.extend(get_segments(m2))
    return state

def main():
    with open('INPUT.TXT', 'r') as f:
        start_time = f.readline().strip()
    
    total_segments = 28
    segment_changes = [set() for _ in range(total_segments)]
    
    time_str = start_time
    hh, mm = map(int, time_str.split(':'))
    total_minutes = 0
    
    while True:
        current_state = get_state(time_str)
        
        for i in range(total_segments):
            segment_changes[i].add(current_state[i])
        
        if all(len(changes) == 2 for changes in segment_changes):
            break
        
        total_minutes += 1
        mm += 1
        if mm == 60:
            mm = 0
            hh += 1
            if hh == 24:
                hh = 0
        
        time_str = f"{hh:02d}:{mm:02d}"
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(total_minutes))

if __name__ == "__main__":
    main()
