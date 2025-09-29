
def main():
    with open('INPUT.TXT', 'r') as f:
        s1 = f.readline().strip()
        s2 = f.readline().strip()
    
    def find_overlap(a, b):
        max_overlap = min(len(a), len(b))
        for i in range(max_overlap, 0, -1):
            if a[-i:].lower() == b[:i].lower():
                return i
        return 0
    
    overlap1 = find_overlap(s1, s2)
    overlap2 = find_overlap(s2, s1)
    
    candidate1 = s1 + s2[overlap1:]
    candidate2 = s2 + s1[overlap2:]
    
    if len(candidate1) < len(candidate2):
        result = candidate1
    elif len(candidate2) < len(candidate1):
        result = candidate2
    else:
        if candidate1.lower() < candidate2.lower():
            result = candidate1
        else:
            result = candidate2
    
    result_chars = list(result.lower())
    result_chars[0] = result_chars[0].upper()
    if overlap1 > 0 and result == candidate1:
        result_chars[len(s1)] = result_chars[len(s1)].upper()
    elif overlap2 > 0 and result == candidate2:
        result_chars[len(s2)] = result_chars[len(s2)].upper()
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(''.join(result_chars))

if __name__ == '__main__':
    main()
