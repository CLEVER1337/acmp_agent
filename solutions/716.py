
def main():
    import sys
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    events = []
    for i in range(1, n):
        parts = data[i].split()
        freq = float(parts[0])
        word = parts[1]
        events.append((freq, word))
    
    low = 30.0
    high = 4000.0
    prev = float(data[1].split()[0])
    
    for i in range(len(events)):
        current, word = events[i]
        if word == 'closer':
            if current > prev:
                low = max(low, (prev + current) / 2)
            else:
                high = min(high, (prev + current) / 2)
        else:
            if current > prev:
                high = min(high, (prev + current) / 2)
            else:
                low = max(low, (prev + current) / 2)
        prev = current
        
    print("{:.6f} {:.6f}".format(low, high))

if __name__ == "__main__":
    main()
