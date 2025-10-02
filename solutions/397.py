
def main():
    s = input().strip()
    n = len(s)
    max_quality = -1
    best_substrings = []
    
    for i in range(n):
        min_char = s[i]
        max_char = s[i]
        for j in range(i, n):
            if s[j] < min_char:
                min_char = s[j]
            if s[j] > max_char:
                max_char = s[j]
                
            quality = ord(max_char) - ord(min_char)
            if quality > max_quality:
                max_quality = quality
                best_substrings = [s[i:j+1]]
            elif quality == max_quality:
                best_substrings.append(s[i:j+1])
    
    best_substrings.sort(key=lambda x: len(x))
    print(best_substrings[0])

if __name__ == "__main__":
    main()
