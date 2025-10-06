
import sys

def read_match(line):
    coords = list(map(int, line.split()))
    return (coords[0], coords[1], coords[2], coords[3])

def normalize_match(match):
    x1, y1, x2, y2 = match
    if (x1, y1) > (x2, y2):
        x1, y1, x2, y2 = x2, y2, x1, y1
    return (x1, y1, x2, y2)

def get_vector(match):
    x1, y1, x2, y2 = match
    return (x2 - x1, y2 - y1)

def main():
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    matches_a = []
    matches_b = []
    
    for i in range(1, 1 + n):
        matches_a.append(read_match(data[i]))
    
    for i in range(1 + n, 1 + 2 * n):
        matches_b.append(read_match(data[i]))
    
    normalized_a = [normalize_match(m) for m in matches_a]
    normalized_b = [normalize_match(m) for m in matches_b]
    
    vecs_a = [get_vector(m) for m in normalized_a]
    vecs_b = [get_vector(m) for m in normalized_b]
    
    vecs_a_sorted = sorted(vecs_a)
    vecs_b_sorted = sorted(vecs_b)
    
    if vecs_a_sorted == vecs_b_sorted:
        print(0)
        return
    
    max_common = 0
    for shift in range(n):
        count = 0
        for i in range(n):
            if vecs_a_sorted[i] == vecs_b_sorted[(i + shift) % n]:
                count += 1
        if count > max_common:
            max_common = count
    
    print(n - max_common)

if __name__ == "__main__":
    main()
