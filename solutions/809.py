
import sys

def read_input():
    data = sys.stdin.read().split()
    n = int(data[0])
    matches_a = []
    matches_b = []
    index = 1
    for i in range(n):
        x1, y1, x2, y2 = map(int, data[index:index+4])
        index += 4
        matches_a.append((x1, y1, x2, y2))
    for i in range(n):
        x1, y1, x2, y2 = map(int, data[index:index+4])
        index += 4
        matches_b.append((x1, y1, x2, y2))
    return n, matches_a, matches_b

def get_center_and_vector(match):
    x1, y1, x2, y2 = match
    cx = (x1 + x2) / 2.0
    cy = (y1 + y2) / 2.0
    dx = x2 - x1
    dy = y2 - y1
    length = (dx**2 + dy**2)**0.5
    return (cx, cy), (dx, dy), length

def normalize_vector(vec, length):
    dx, dy = vec
    if length > 1e-9:
        return (dx/length, dy/length)
    return (0.0, 0.0)

def main():
    n, matches_a, matches_b = read_input()
    
    centers_a = []
    vectors_a = []
    lengths_a = []
    for match in matches_a:
        center, vec, length = get_center_and_vector(match)
        centers_a.append(center)
        vectors_a.append(normalize_vector(vec, length))
        lengths_a.append(length)
    
    centers_b = []
    vectors_b = []
    lengths_b = []
    for match in matches_b:
        center, vec, length = get_center_and_vector(match)
        centers_b.append(center)
        vectors_b.append(normalize_vector(vec, length))
        lengths_b.append(length)
    
    lengths_a_sorted = sorted(lengths_a)
    lengths_b_sorted = sorted(lengths_b)
    
    if lengths_a_sorted != lengths_b_sorted:
        print(n)
        return
    
    best_match_count = 0
    
    for i in range(n):
        dx = centers_b[0][0] - centers_a[i][0]
        dy = centers_b[0][1] - centers_a[i][1]
        
        used = [False] * n
        match_count = 0
        
        for j in range(n):
            target_center_x = centers_a[j][0] + dx
            target_center_y = centers_a[j][1] + dy
            
            found = False
            for k in range(n):
                if not used[k]:
                    if abs(target_center_x - centers_b[k][0]) < 1e-9 and abs(target_center_y - centers_b[k][1]) < 1e-9:
                        if abs(vectors_a[j][0] - vectors_b[k][0]) < 1e-9 and abs(vectors_a[j][1] - vectors_b[k][1]) < 1e-9:
                            used[k] = True
                            match_count += 1
                            found = True
                            break
            if not found:
                for k in range(n):
                    if not used[k]:
                        if abs(target_center_x - centers_b[k][0]) < 1e-9 and abs(target_center_y - centers_b[k][1]) < 1e-9:
                            if abs(vectors_a[j][0] + vectors_b[k][0]) < 1e-9 and abs(vectors_a[j][1] + vectors_b[k][1]) < 1e-9:
                                used[k] = True
                                match_count += 1
                                break
        
        if match_count > best_match_count:
            best_match_count = match_count
    
    for i in range(n):
        dx = centers_b[0][0] - (centers_a[i][0] + vectors_a[i][0] * lengths_a[i] / 2)
        dy = centers_b[0][1] - (centers_a[i][1] + vectors_a[i][1] * lengths_a[i] / 2)
        
        used = [False] * n
        match_count = 0
        
        for j in range(n):
            end_x = centers_a[j][0] + vectors_a[j][0] * lengths_a[j] / 2
            end_y = centers_a[j][1] + vectors_a[j][1] * lengths_a[j] / 2
            target_end_x = end_x + dx
            target_end_y = end_y + dy
            
            found = False
            for k in range(n):
                if not used[k]:
                    end_b_x = centers_b[k][0] + vectors_b[k][0] * lengths_b[k] / 2
                    end_b_y = centers_b[k][1] + vectors_b[k][1] * lengths_b[k] / 2
                    if abs(target_end_x - end_b_x) < 1e-9 and abs(target_end_y - end_b_y) < 1e-9:
                        rev_vec = (-vectors_a[j][0], -vectors_a[j][1])
                        if abs(rev_vec[0] - vectors_b[k][0]) < 1e-9 and abs(rev_vec[1] - vectors_b[k][1]) < 1e-9:
                            used[k] = True
                            match_count += 1
                            found = True
                            break
            if not found:
                for k in range(n):
                    if not used[k]:
                        end_b_x = centers_b[k][0] + vectors_b[k][0] * lengths_b[k] / 2
                        end_b_y = centers_b[k][1] + vectors_b[k][1] * lengths_b[k] / 2
                        if abs(target_end_x - end_b_x) < 1e-9 and abs(target_end_y - end_b_y) < 1e-9:
                            rev_vec = (-vectors_a[j][0], -vectors_a[j][1])
                            rev_vec_b = (-vectors_b[k][0], -vectors_b[k][1])
                            if abs(rev_vec[0] - rev_vec_b[0]) < 1e-9 and abs(rev_vec[1] - rev_vec_b[1]) < 1e-9:
                                used[k] = True
                                match_count += 1
                                break
        
        if match_count > best_match_count:
            best_match_count = match_count
    
    print(n - best_match_count)

if __name__ == "__main__":
    main()
