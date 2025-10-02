
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
            if pos < len(char):
                return char[pos]
            return '-'
        
        if char not in 'ABCDEFGHIJ'[:n]:
            return '-'
            
        idx = ord(char) - ord('A')
        expansion = morphisms[idx]
        
        for c in expansion:
            if pos < len_expansion(c, k_level - 1):
                return get_char(pos, k_level - 1, c)
            pos -= len_expansion(c, k_level - 1)
        
        return '-'
    
    memo = {}
    def len_expansion(char, k_level):
        if k_level == 0:
            return 1
            
        key = (char, k_level)
        if key in memo:
            return memo[key]
            
        if char not in 'ABCDEFGHIJ'[:n]:
            memo[key] = 0
            return 0
            
        idx = ord(char) - ord('A')
        expansion = morphisms[idx]
        total = 0
        for c in expansion:
            total += len_expansion(c, k_level - 1)
            
        memo[key] = total
        return total
    
    pos = p - 1
    for char in w:
        char_len = len_expansion(char, k)
        if pos < char_len:
            result = get_char(pos, k, char)
            print(result)
            return
        pos -= char_len
        
    print('-')

if __name__ == "__main__":
    main()
