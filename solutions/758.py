
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    speeds = list(map(int, data[1:1+n]))
    
    if n == 0:
        print(0)
        return
    if n == 1:
        print(speeds[0])
        return
        
    speeds.sort()
    total_time = 0
    i = n - 1
    
    while i >= 3:
        option1 = speeds[0] + 2 * speeds[1] + speeds[i]
        option2 = 2 * speeds[0] + speeds[i] + speeds[i-1]
        total_time += min(option1, option2)
        i -= 2
        
    if i == 2:
        total_time += speeds[0] + speeds[1] + speeds[2]
    elif i == 1:
        total_time += speeds[1]
    else:
        total_time += speeds[0]
        
    print(total_time)

if __name__ == "__main__":
    main()
