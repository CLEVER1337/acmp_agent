
def main():
    import sys
    data = sys.stdin.read().splitlines()
    if not data:
        print('-')
        return
        
    n, k, p = map(int, data[0].split())
    w = data[1].strip()
    morphisms = []
    for i in range(2, 2 + n):
        morphisms.append(data[i].strip())
    
    def get_char(pos, k_level, char):
        if k_level == 0:
            if pos <= len(char):
                return char[pos - 1]
            return '-'
        
        if char.isalpha():
            char_idx = ord(char) - ord('A')
            if char_idx < 0 or char_idx >= len(morphisms):
                return '-'
            morph = morphisms[char_idx]
        else:
            morph = char
            
        if k_level == 0:
            if pos <= len(morph):
                return morph[pos - 1]
            return '-'
        
        total_len = 0
        for c in morph:
            if k_level == 0:
                char_len = 1
            else:
                if c.isalpha():
                    char_idx = ord(c) - ord('A')
                    if char_idx < 0 or char_idx >= len(morphisms):
                        char_len = 1
                    else:
                        char_len = len(get_expanded_length(c, k_level - 1))
                else:
                    char_len = 1
            
            if total_len + char_len >= pos:
                return get_char(pos - total_len, k_level - 1, c)
            total_len += char_len
        
        return '-'
    
    def get_expanded_length(s, level):
        if level == 0:
            return s
            
        result = []
        for char in s:
            if char.isalpha():
                char_idx = ord(char) - ord('A')
                if 0 <= char_idx < len(morphisms):
                    result.append(get_expanded_length(morphisms[char_idx], level - 1))
                else:
                    result.append(char)
            else:
                result.append(char)
        return ''.join(result)
    
    if k == 0:
        if p <= len(w):
            print(w[p - 1])
        else:
            print('-')
        return
            
    total_len = 0
    for char in w:
        if k == 0:
            char_len = 1
        else:
            if char.isalpha():
                char_idx = ord(char) - ord('A')
                if char_idx < 0 or char_idx >= len(morphisms):
                    char_len = 1
                else:
                    char_len = len(get_expanded_length(morphisms[char_idx], k - 1))
            else:
                char_len = 1
        
        if total_len + char_len >= p:
            result_char = get_char(p - total_len, k - 1, char)
            print(result_char)
            return
        total_len += char_len
    
    print('-')

if __name__ == "__main__":
    main()
