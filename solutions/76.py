
def main():
    n = int(input().strip())
    events = []
    for _ in range(n):
        start, end = input().split()
        h1, m1 = map(int, start.split(':'))
        h2, m2 = map(int, end.split(':'))
        time_in = h1 * 60 + m1
        time_out = h2 * 60 + m2
        events.append((time_in, 1))
        events.append((time_out, -1))
    
    events.sort()
    
    max_count = 0
    current_count = 0
    
    for event in events:
        current_count += event[1]
        if current_count > max_count:
            max_count = current_count
            
    print(max_count)

if __name__ == "__main__":
    main()
