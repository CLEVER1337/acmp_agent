
def main():
    s = input().strip()
    n = len(s)
    max_len = 0
    
    for i in range(n):
        for j in range(i + 1, n):
            length = j - i + 1
            if length <= max_len:
                continue
                
            substr1 = s[i:j+1]
            count1 = [0] * 26
            for c in substr1:
                count1[ord(c) - ord('a')] += 1
                
            for k in range(i + 1, n - length + 1):
                substr2 = s[k:k+length]
                count2 = [0] * 26
                for c in substr2:
                    count2[ord(c) - ord('a')] += 1
                    
                match = True
                for idx in range(26):
                    if count1[idx] != count2[idx]:
                        match = False
                        break
                        
                if match:
                    max_len = max(max_len, length)
                    break
                    
    print(max_len)

if __name__ == "__main__":
    main()
