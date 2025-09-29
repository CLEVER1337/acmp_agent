
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    rects = []
    index = 1
    
    for i in range(n):
        x1 = int(data[index]); y1 = int(data[index+1])
        x2 = int(data[index+2]); y2 = int(data[index+3])
        index += 4
        rects.append((min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)))
    
    events = []
    xs = set()
    ys = set()
    
    for x1, y1, x2, y2 in rects:
        xs.add(x1)
        xs.add(x2)
        ys.add(y1)
        ys.add(y2)
        events.append((x1, y1, y2, 1))
        events.append((x2, y1, y2, -1))
    
    xs = sorted(xs)
    ys = sorted(ys)
    
    m = len(ys)
    cnt = [0] * (m)
    
    res = 0
    for i in range(len(xs) - 1):
        cur_events = []
        for event in events:
            if event[0] == xs[i]:
                cur_events.append((event[1], event[2], event[3]))
        
        cur_events.sort()
        
        for j in range(m - 1):
            cover = 0
            for y1, y2, type in cur_events:
                if y1 <= ys[j] and y2 >= ys[j+1]:
                    cover += type
            
            if cover > 0:
                cnt[j] += 1
        
        for j in range(m - 1):
            if cnt[j] > 0:
                res += (xs[i+1] - xs[i]) * (ys[j+1] - ys[j])
        
        for event in events:
            if event[0] == xs[i+1]:
                y1, y2, type = event[1], event[2], event[3]
                for j in range(m - 1):
                    if y1 <= ys[j] and y2 >= ys[j+1]:
                        cnt[j] += type
    
    print(res)

if __name__ == "__main__":
    main()
