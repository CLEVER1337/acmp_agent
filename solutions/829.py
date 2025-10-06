
def main():
    a = input().strip()
    b = input().strip()
    n = len(a)
    m = len(b)
    
    if m == 0:
        print(0)
        return
        
    if n < m:
        print(0)
        return
        
    s = b + '#' + a + a
    lps = [0] * len(s)
    length = 0
    i = 1
    total = 0
    
    while i < len(s):
        if s[i] == s[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
                
    for i in range(2 * m + 1, len(s)):
        if lps[i] == m:
            total += 1
            
    print(total)

if __name__ == "__main__":
    main()
