
def main():
    import sys
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    events = []
    
    for i in range(1, n + 1):
        line = data[i].split()
        start = list(map(int, line[0].split(':')))
        end = list(map(int, line[1].split(':')))
        
        start_minutes = start[0] * 60 + start[1]
        end_minutes = end[0] * 60 + end[1]
        
        events.append((start_minutes, 1))
        events.append((end_minutes, -1))
    
    events.sort()
    
    current = 0
    max_visitors = 0
    
    for event in events:
        current += event[1]
        if current > max_visitors:
            max_visitors = current
            
    print(max_visitors)

if __name__ == "__main__":
    main()
