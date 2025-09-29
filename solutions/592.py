
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    m = int(data[0])
    index = 1
    columns = []
    
    for _ in range(m):
        ai = int(data[index])
        index += 1
        segments = []
        for j in range(ai):
            l = int(data[index])
            r = int(data[index + 1])
            index += 2
            segments.append((l, r))
        columns.append(segments)
    
    n = 0
    for segs in columns:
        if segs:
            max_r = max(r for _, r in segs)
            n = max(n, max_r)
    
    fall_height = [0] * (n + 2)
    result = []
    
    for segs in columns:
        max_top = 0
        for l, r in segs:
            max_fall = 0
            for pos in range(l, r + 1):
                if fall_height[pos] > max_fall:
                    max_fall = fall_height[pos]
            new_height = max_fall + (r - l + 1)
            for pos in range(l, r + 1):
                fall_height[pos] = new_height
            if new_height > max_top:
                max_top = new_height
        result.append(str(max_top))
    
    sys.stdout.write("\n".join(result))

if __name__ == "__main__":
    main()
