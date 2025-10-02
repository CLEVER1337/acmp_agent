
def main():
    with open('INPUT.TXT', 'r') as f:
        n = int(f.readline().strip())
        colors = list(map(int, f.readline().split()))
    
    count = {}
    for color in colors:
        count[color] = count.get(color, 0) + 1
    
    max_count = max(count.values())
    candidates = [color for color, cnt in count.items() if cnt == max_count]
    
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
