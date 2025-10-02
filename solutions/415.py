
def main():
    with open('INPUT.TXT', 'r') as f:
        s1 = f.readline().strip()
        s2 = f.readline().strip()
    
    def find_overlap(a, b):
        max_overlap = 0
        n = min(len(a), len(b))
        for i in range(n, 0, -1):
            if a[-i:].lower() == b[:i].lower():
                max_overlap = i
                break
        return max_overlap
    
    overlap1 = find_overlap(s1, s2)
    overlap2 = find_overlap(s2, s1)
    
    candidate1 = s1 + s2[overlap1:]
    candidate2 = s2 + s1[overlap2:]
    
    if len(candidate1) < len(candidate2):
        result = candidate1
    elif len(candidate2) < len(candidate1):
        result = candidate2
    else:
        result = min(candidate1, candidate2)
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(result)

if __name__ == '__main__':
    main()
