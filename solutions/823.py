
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    points = []
    for i in range(n):
        x = int(data[2*i+1])
        y = int(data[2*i+2])
        points.append((x, y))
    
    if n == 0:
        print(0)
        return
        
    points.sort()
    min_x = min(p[0] for p in points)
    max_x = max(p[0] for p in points)
    
    left = {}
    right = {}
    for x, y in points:
        if x not in left:
            left[x] = y
            right[x] = y
        else:
            if y < left[x]:
                left[x] = y
            if y > right[x]:
                right[x] = y
                
    cols = sorted(left.keys())
    dp = {}
    for i, x in enumerate(cols):
        if i == 0:
            dp[(x, left[x])] = (x - 1) + (right[x] - left[x]) + (right[x] - 1)
            dp[(x, right[x])] = (x - 1) + (right[x] - left[x]) + (right[x] - 1)
            continue
            
        prev_x = cols[i-1]
        for pos in [left[prev_x], right[prev_x]]:
            if (prev_x, pos) not in dp:
                continue
                
            current_dist = dp[(prev_x, pos)]
            dist_to_left = abs(pos - left[x]) + (x - prev_x)
            dist_to_right = abs(pos - right[x]) + (x - prev_x)
            
            total_left = current_dist + dist_to_left + (right[x] - left[x])
            total_right = current_dist + dist_to_right + (right[x] - left[x])
            
            if (x, right[x]) not in dp or total_left < dp[(x, right[x])]:
                dp[(x, right[x])] = total_left
            if (x, left[x]) not in dp or total_right < dp[(x, left[x])]:
                dp[(x, left[x])] = total_right
                
    last_x = cols[-1]
    result = min(dp.get((last_x, left[last_x]), float('inf')), dp.get((last_x, right[last_x]), float('inf')))
    print(result)

if __name__ == "__main__":
    main()
