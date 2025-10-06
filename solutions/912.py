
def main():
    n = int(input().strip())
    arr = list(map(int, input().split()))
    
    count = {}
    for num in arr:
        count[num] = count.get(num, 0) + 1
        
    max_count = 0
    candidates = []
    
    for color, cnt in count.items():
        if cnt > max_count:
            max_count = cnt
            candidates = [color]
        elif cnt == max_count:
            candidates.append(color)
            
    if len(candidates) == 1:
        print(candidates[0])
    else:
        if 0 in candidates:
            print(0)
        else:
            print(min(candidates))

if __name__ == "__main__":
    main()
