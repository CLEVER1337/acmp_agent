
import sys

def main():
    data = sys.stdin.read().splitlines()
    if not data:
        print('-')
        return
        
    n, k, p = map(int, data[0].split())
    w = data[1].strip()
    mappings = {}
    letters = 'ABCDEFGHIJ'[:n]
    
    for i, letter in enumerate(letters):
        if i + 2 < len(data):
            mappings[letter] = data[i + 2].strip()
        else:
            mappings[letter] = ""
            
    def get_length(level, char):
        if level == 0:
            return 1
        if char not in mappings:
            return 0
            
        total = 0
        for c in mappings[char]:
            total += get_length(level - 1, c)
            if total > p:
                break
        return total

    def find_char(level, char, pos):
        if level == 0:
            return char if pos == 1 else None
            
        if char not in mappings:
            return None
            
        current_pos = 1
        for c in mappings[char]:
            length = get_length(level - 1, c)
            if pos >= current_pos and pos < current_pos + length:
                return find_char(level - 1, c, pos - current_pos + 1)
            current_pos += length
        return None

    result = None
    current_pos = 1
    for char in w:
        length = get_length(k, char)
        if p >= current_pos and p < current_pos + length:
            result = find_char(k, char, p - current_pos + 1)
            break
        current_pos += length
        
    print(result if result is not None else '-')

if __name__ == "__main__":
    main()
