
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

def normalize_match(x1, y1, x2, y2):
    if (x1, y1) > (x2, y2):
        x1, y1, x2, y2 = x2, y2, x1, y1
    dx, dy = x2 - x1, y2 - y1
    return (dx, dy)

def main():
    n, matches_a, matches_b = read_input()
    
    normalized_a = []
    for match in matches_a:
        x1, y1, x2, y2 = match
        normalized_a.append(normalize_match(x1, y1, x2, y2))
    
    normalized_b = []
    for match in matches_b:
        x1, y1, x2, y2 = match
        normalized_b.append(normalize_match(x1, y1, x2, y2))
    
    normalized_a.sort()
    normalized_b.sort()
    
    count = 0
    for i in range(n):
        if normalized_a[i] != normalized_b[i]:
            count += 1
    
    print(count)

if __name__ == "__main__":
    main()
