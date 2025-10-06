
def main():
    import sys
    data = sys.stdin.readline().split()
    n = int(data[0])
    m = int(data[1])
    bends = data[2:2+m]
    
    segments = [(i, 'F') for i in range(n+1)]
    
    for bend_str in bends:
        bend_point = int(bend_str[:-1])
        direction = bend_str[-1]
        
        if bend_point > len(segments) - 1:
            print("SCRUFFY")
            return
            
        left = segments[:bend_point]
        right = segments[bend_point:]
        
        if direction == 'F':
            right = [(seg[0], 'R' if seg[1] == 'F' else 'F') for seg in reversed(right)]
        else:
            right = [(seg[0], 'F' if seg[1] == 'R' else 'R') for seg in reversed(right)]
            
        segments = left + right
        
    visible_f = []
    visible_r = []
    seen = set()
    
    for seg in segments:
        if seg[0] not in seen:
            seen.add(seg[0])
            if seg[1] == 'F':
                visible_f.append(seg[0])
            else:
                visible_r.append(seg[0])
                
    visible_f.sort()
    visible_r.sort()
    
    result = []
    for seg in visible_f:
        result.append(f"P{seg}F")
    for seg in visible_r:
        result.append(f"P{seg}R")
        
    print(" ".join(result))

if __name__ == "__main__":
    main()
