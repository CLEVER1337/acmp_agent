
def main():
    import sys
    data = sys.stdin.read().splitlines()
    K = int(data[0].strip())
    s = data[1].strip()
    
    if K == 0:
        print(s)
        return
        
    n = len(s)
    chars = list(s)
    result = [''] * n
    
    positions = [[] for _ in range(26)]
    for i, c in enumerate(chars):
        idx = ord(c) - ord('a')
        positions[idx].append(i)
    
    for char_idx in range(26):
        if not positions[char_idx]:
            continue
            
        indices = positions[char_idx]
        group_size = len(indices)
        
        if group_size == 1:
            pos = indices[0]
            result[pos] = chr(ord('a') + char_idx)
            continue
            
        ranges = []
        for i in indices:
            left = max(0, i - K)
            right = min(n - 1, i + K)
            ranges.append((left, right))
            
        merged = []
        start, end = ranges[0]
        for i in range(1, group_size):
            if ranges[i][0] <= end + 1:
                end = max(end, ranges[i][1])
            else:
                merged.append((start, end))
                start, end = ranges[i]
        merged.append((start, end))
        
        segments = []
        current_start = merged[0][0]
        current_end = merged[0][1]
        segment_chars = 1
        
        for i in range(1, len(merged)):
            if merged[i][0] - current_end - 1 < group_size - segment_chars:
                current_end = merged[i][1]
                segment_chars += 1
            else:
                segments.append((current_start, current_end, segment_chars))
                current_start, current_end = merged[i]
                segment_chars = 1
        segments.append((current_start, current_end, segment_chars))
        
        pos_ptr = 0
        for seg_start, seg_end, seg_count in segments:
            available_positions = seg_end - seg_start + 1
            step = (available_positions - 1) / (seg_count - 1) if seg_count > 1 else 0
            
            for i in range(seg_count):
                pos = round(seg_start + i * step)
                result[pos] = chr(ord('a') + char_idx)
                pos_ptr += 1
    
    print(''.join(result))

if __name__ == '__main__':
    main()
