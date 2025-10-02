
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
    
    heights = [0] * m
    stable_segments = []
    
    for col_idx, segments in enumerate(columns):
        if not segments:
            heights[col_idx] = 0
            continue
        
        max_height = 0
        for l, r in segments:
            if r > max_height:
                max_height = r
        heights[col_idx] = max_height
    
    for col_idx in range(m):
        if heights[col_idx] == 0:
            continue
            
        segments = columns[col_idx]
        max_fall = 0
        
        for l, r in segments:
            fall_distance = l - 1
            for stable_seg in stable_segments:
                if stable_seg[0] <= col_idx <= stable_seg[1]:
                    if stable_seg[2] >= l - 1:
                        fall_distance = min(fall_distance, l - stable_seg[2] - 1)
            
            if fall_distance > 0:
                new_l = l - fall_distance
                new_r = r - fall_distance
                if new_l <= 1:
                    stable_segments.append((col_idx, col_idx, new_r))
                else:
                    for i in range(len(stable_segments)):
                        seg = stable_segments[i]
                        if seg[0] <= col_idx <= seg[1] and seg[2] >= new_l - 1:
                            stable_segments[i] = (min(seg[0], col_idx), max(seg[1], col_idx), max(seg[2], new_r))
                            break
                    else:
                        stable_segments.append((col_idx, col_idx, new_r))
            
            heights[col_idx] = min(heights[col_idx], r - fall_distance)
    
    for col_idx in range(m):
        segments = columns[col_idx]
        if not segments:
            print(0, end=' ')
            continue
            
        max_r = 0
        for l, r in segments:
            if r > max_r:
                max_r = r
                
        fall = max_r
        for seg in stable_segments:
            if seg[0] <= col_idx <= seg[1]:
                if seg[2] < max_r:
                    fall = min(fall, max_r - (max_r - seg[2]))
                else:
                    fall = min(fall, max_r)
        
        print(fall, end=' ')

if __name__ == "__main__":
    main()
