
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    events = []
    for i in range(1, len(data), 2):
        a = int(data[i])
        b = int(data[i+1])
        events.append((a, 1))
        events.append((b, -1))
    
    events.sort()
    
    current_color = 0
    last_pos = 0
    max_white = 0
    count = 0
    
    for pos, event_type in events:
        if current_color == 0:
            white_segment = pos - last_pos
            if white_segment > max_white:
                max_white = white_segment
        
        count += event_type
        current_color = count % 2
        last_pos = pos
    
    if current_color == 0:
        white_segment = 10**9 - last_pos
        if white_segment > max_white:
            max_white = white_segment
            
    print(max_white)

if __name__ == "__main__":
    main()
