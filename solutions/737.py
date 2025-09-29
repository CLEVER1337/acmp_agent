
def main():
    with open("INPUT.TXT", "r") as f:
        s1 = f.readline().strip()
        s2 = f.readline().strip()
    
    n, m = len(s1), len(s2)
    max_len = 0
    pos_i, pos_j = 0, 0
    
    for i in range(n):
        for j in range(m):
            length = min(n - i, m - j)
            if length <= max_len:
                continue
                
            count1 = [0] * 4
            count2 = [0] * 4
            
            for k in range(length):
                c1 = s1[i + k]
                idx1 = 0
                if c1 == 'C': idx1 = 1
                elif c1 == 'G': idx1 = 2
                elif c1 == 'T': idx1 = 3
                count1[idx1] += 1
                
                c2 = s2[j + k]
                idx2 = 0
                if c2 == 'C': idx2 = 1
                elif c2 == 'G': idx2 = 2
                elif c2 == 'T': idx2 = 3
                count2[idx2] += 1
                
                if count1 == count2 and k + 1 > max_len:
                    max_len = k + 1
                    pos_i, pos_j = i, j
    
    with open("OUTPUT.TXT", "w") as f:
        f.write(str(max_len) + "\n")
        if max_len > 0:
            f.write(f"{pos_i + 1} {pos_j + 1}\n")

if __name__ == "__main__":
    main()
