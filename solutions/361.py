
def main():
    s = input().strip()
    n = len(s)
    max_len = 0
    
    for i in range(n):
        for j in range(i + 1, n + 1):
            sub1 = s[i:j]
            freq1 = [0] * 26
            for c in sub1:
                freq1[ord(c) - ord('a')] += 1
                
            for k in range(i + 1, n):
                for l in range(k + len(sub1), n + 1):
                    sub2 = s[k:l]
                    if len(sub2) != len(sub1):
                        continue
                    freq2 = [0] * 26
                    for c in sub2:
                        freq2[ord(c) - ord('a')] += 1
                    
                    if freq1 == freq2:
                        max_len = max(max_len, len(sub1))
    
    print(max_len)

if __name__ == "__main__":
    main()
