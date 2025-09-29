
def main():
    with open('INPUT.TXT', 'r') as f:
        s1 = f.readline().strip()
        s2 = f.readline().strip()
    
    n1, n2 = len(s1), len(s2)
    min_len = n1 + n2
    
    for shift in range(-n2 + 1, n1):
        valid = True
        for i in range(max(0, -shift), min(n1 - shift, n2)):
            if int(s1[i + shift]) + int(s2[i]) > 3:
                valid = False
                break
        if valid:
            overlap_start = max(0, -shift)
            overlap_end = min(n1 - shift, n2)
            overlap = overlap_end - overlap_start
            total_len = n1 + n2 - overlap
            if total_len < min_len:
                min_len = total_len
    
    print(min_len)

if __name__ == '__main__':
    main()
