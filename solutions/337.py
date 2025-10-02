
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    k = int(data[1])
    periods = list(map(int, data[2:2+k]))
    
    lamps = {}
    for p in periods:
        step = p
        start = step
        while start <= n:
            lamps[start] = lamps.get(start, 0) + 1
            start += step
    
    count = 0
    for state in lamps.values():
        if state % 2 == 1:
            count += 1
            
    print(count)

if __name__ == "__main__":
    main()
