
def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        print(0)
        return
        
    n = int(data[0])
    events = []
    for i in range(n):
        a = int(data[1 + 2*i])
        b = int(data[2 + 2*i])
        events.append((a, 1))
        events.append((b, -1))
        
    events.sort()
    
    balance = 0
    start = None
    max_len = 0
    prev_pos = 0
    
    for pos, event_type in events:
        if balance == 0:
            if start is not None:
                white_len = pos - start
                if white_len > max_len:
                    max_len = white_len
            start = pos
            
        balance += event_type
        
        if balance == 0:
            start = pos
            
    if balance == 0 and start is not None:
        white_len = 10**9 - start
        if white_len > max_len:
            max_len = white_len
            
    print(max_len)

if __name__ == "__main__":
    main()
