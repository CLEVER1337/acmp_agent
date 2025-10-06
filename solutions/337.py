
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        print(0)
        return
        
    N = int(data[0])
    K = int(data[1])
    periods = list(map(int, data[2:2+K]))
    
    events = []
    for p in periods:
        events.append(p)
        
    events.sort()
    unique_periods = []
    for p in events:
        if not unique_periods or p != unique_periods[-1]:
            unique_periods.append(p)
            
    periods = unique_periods
    K = len(periods)
    
    stack = []
    for i in range(K):
        current = periods[i]
        count = 0
        for j in range(i+1, K):
            if periods[j] % current == 0:
                count += 1
        if count % 2 == 0:
            stack.append(current)
        else:
            stack.append(-current)
            
    result = 0
    for p in stack:
        if p > 0:
            result += N // p
        else:
            result -= N // (-p)
            
    print(result)

if __name__ == "__main__":
    main()
