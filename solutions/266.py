
def main():
    with open('INPUT.TXT', 'r') as f:
        n = int(f.readline().strip())
        intervals = []
        for _ in range(n):
            data = list(map(int, f.readline().split()))
            h1, m1, h2, m2 = data
            start = h1 * 60 + m1
            end = h2 * 60 + m2
            
            if start == end:
                intervals.append((0, 1440))
            elif start < end:
                intervals.append((start, end))
            else:
                intervals.append((start, 1440))
                intervals.append((0, end))
    
    if not intervals:
        print(0)
        return
        
    timeline = [0] * 1441
    for start, end in intervals:
        timeline[start] += 1
        timeline[end] -= 1
        
    current = 0
    total_time = 0
    for i in range(1440):
        current += timeline[i]
        if current == n:
            total_time += 1
            
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(total_time))

if __name__ == '__main__':
    main()
