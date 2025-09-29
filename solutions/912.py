
from collections import Counter

def main():
    with open('INPUT.TXT', 'r') as f:
        n = int(f.readline().strip())
        colors = list(map(int, f.readline().split()))
    
    counter = Counter(colors)
    max_count = max(counter.values())
    
    candidates = [color for color, count in counter.items() if count == max_count]
    
    if len(candidates) == 1:
        result = candidates[0]
    else:
        if 0 in candidates:
            result = 0
        else:
            result = min(candidates)
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(result))

if __name__ == '__main__':
    main()
