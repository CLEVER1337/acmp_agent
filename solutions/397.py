
def main():
    s = input().strip()
    n = len(s)
    max_quality = -1
    best_sub = ""
    
    for i in range(n):
        min_char = ord(s[i])
        max_char = ord(s[i])
        
        for j in range(i, n):
            c = ord(s[j])
            if c < min_char:
                min_char = c
            if c > max_char:
                max_char = c
                
            quality = max_char - min_char
            length = j - i + 1
            
            if quality > max_quality:
                max_quality = quality
                best_sub = s[i:j+1]
            elif quality == max_quality:
                if length < len(best_sub):
                    best_sub = s[i:j+1]
    
    print(best_sub)

if __name__ == "__main__":
    main()
