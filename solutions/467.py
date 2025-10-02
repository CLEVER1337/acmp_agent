
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    events = []
    for i in range(n):
        a = int(data[1 + 2*i])
        b = int(data[2 + 2*i])
        events.append((a, 1))
        events.append((b, -1))
    
    events.sort()
    
    balance = 0
    start_white = None
    max_white_len = 0
    prev = 0
    
    for pos, event_type in events:
        if balance == 0:
            white_len = pos - prev
            if white_len > max_white_len:
                max_white_len = white_len
            start_white = pos
        elif balance == 1 and event_type == -1:
            start_white = pos
        
        balance += event_type
        
        if balance == 0:
            prev = pos
    
    if balance == 0:
        white_len = 10**9 - prev
        if white_len > max_white_len:
            max_white_len = white_len
    
    print(max_white_len)

if __name__ == "__main__":
    main()
