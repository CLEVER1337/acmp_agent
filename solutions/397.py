
def main():
    s = input().strip()
    n = len(s)
    max_quality = -1
    best_sub = ""
    
    for i in range(n):
        min_char = s[i]
        max_char = s[i]
        
        for j in range(i, n):
            if s[j] < min_char:
                min_char = s[j]
            if s[j] > max_char:
                max_char = s[j]
                
            quality = ord(max_char) - ord(min_char)
            substr = s[i:j+1]
            
            if quality > max_quality:
                max_quality = quality
                best_sub = substr
            elif quality == max_quality:
                if len(substr) < len(best_sub):
                    best_sub = substr
                    
    print(best_sub)

if __name__ == "__main__":
    main()
