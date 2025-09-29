
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    segments = []
    index = 1
    for i in range(n):
        l = int(data[index])
        r = int(data[index + 1])
        index += 2
        segments.append((l, r))
    
    segments.sort()
    
    total_length = 0
    current_start = segments[0][0]
    current_end = segments[0][1]
    
    for i in range(1, n):
        if segments[i][0] <= current_end:
            current_end = max(current_end, segments[i][1])
        else:
            total_length += current_end - current_start
            current_start = segments[i][0]
            current_end = segments[i][1]
    
    total_length += current_end - current_start
    
    print(total_length)

if __name__ == "__main__":
    main()
