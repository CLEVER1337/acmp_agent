
def main():
    with open('INPUT.TXT', 'r') as f:
        s1 = f.readline().strip()
        s2 = f.readline().strip()
    
    n1, n2 = len(s1), len(s2)
    max_len = 0
    pos1, pos2 = 0, 0
    
    for i in range(n1):
        for j in range(n2):
            l = 0
            count1 = [0] * 4
            count2 = [0] * 4
            while i + l < n1 and j + l < n2:
                c1 = s1[i + l]
                c2 = s2[j + l]
                idx1 = 'ACGT'.index(c1)
                idx2 = 'ACGT'.index(c2)
                count1[idx1] += 1
                count2[idx2] += 1
                if count1 == count2:
                    if l + 1 > max_len:
                        max_len = l + 1
                        pos1, pos2 = i, j
                l += 1
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(max_len) + '\n')
        if max_len > 0:
            f.write(f"{pos1} {pos2}\n")

if __name__ == '__main__':
    main()
