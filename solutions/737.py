
def main():
    s1 = input().strip()
    s2 = input().strip()
    n1, n2 = len(s1), len(s2)
    max_len = 0
    pos1 = 0
    pos2 = 0
    
    for i in range(n1):
        for j in range(n2):
            l = 0
            cnt1 = [0] * 4
            cnt2 = [0] * 4
            while i + l < n1 and j + l < n2:
                c1 = s1[i + l]
                c2 = s2[j + l]
                idx1 = ord(c1) % 4
                idx2 = ord(c2) % 4
                cnt1[idx1] += 1
                cnt2[idx2] += 1
                if cnt1 == cnt2:
                    if l + 1 > max_len:
                        max_len = l + 1
                        pos1 = i
                        pos2 = j
                l += 1
                
    print(max_len)
    if max_len > 0:
        print(pos1, pos2)

if __name__ == "__main__":
    main()
