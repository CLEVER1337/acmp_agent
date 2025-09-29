
def main():
    with open('INPUT.TXT', 'r') as f:
        s = f.readline().strip()
    
    n = len(s)
    counts = [0] * 26
    
    for c in s:
        idx = ord(c) - ord('A')
        counts[idx] += 1
    
    prefix_sum = 0
    for i in range(26):
        prefix_sum += counts[i]
        if prefix_sum < i + 1:
            print("NO")
            return
    
    result = []
    positions = [[] for _ in range(26)]
    
    for idx, c in enumerate(s, 1):
        pos = ord(c) - ord('A')
        positions[pos].append(idx)
    
    current = 0
    for i in range(26):
        while current < 26 and len(positions[current]) == 0:
            current += 1
        if current < 26:
            result.append(str(positions[current].pop()))
        else:
            break
    
    print("YES")
    print(" ".join(result))

if __name__ == "__main__":
    main()
