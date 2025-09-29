
def main():
    import sys
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    events = []
    
    for i in range(1, n + 1):
        line = data[i].split()
        start_time = line[0]
        end_time = line[1]
        
        start_h, start_m = map(int, start_time.split(':'))
        end_h, end_m = map(int, end_time.split(':'))
        
        start_total = start_h * 60 + start_m
        end_total = end_h * 60 + end_m
        
        events.append((start_total, 1))
        events.append((end_total, -1))
    
    events.sort()
    
    current_visitors = 0
    max_visitors = 0
    
    for event in events:
        current_visitors += event[1]
        if current_visitors > max_visitors:
            max_visitors = current_visitors
            
    print(max_visitors)

if __name__ == "__main__":
    main()
