
def main():
    import sys
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    lines = data[1:1+n]
    
    key_phrase = "the quick brown fox jumps over the lazy dog"
    key_words = key_phrase.split()
    
    mapping = None
    for i, line in enumerate(lines):
        words = line.split()
        if len(words) != len(key_words):
            continue
            
        valid = True
        temp_mapping = {}
        
        for j in range(len(words)):
            if len(words[j]) != len(key_words[j]):
                valid = False
                break
                
            for k in range(len(words[j])):
                cipher_char = words[j][k]
                plain_char = key_words[j][k]
                
                if cipher_char in temp_mapping:
                    if temp_mapping[cipher_char] != plain_char:
                        valid = False
                        break
                else:
                    temp_mapping[cipher_char] = plain_char
        
        if valid and len(temp_mapping) == 26:
            mapping = temp_mapping
            break
    
    if mapping is None:
        print("No solution")
        return
        
    result = []
    for line in lines:
        decrypted = []
        for char in line:
            if char == ' ':
                decrypted.append(' ')
            else:
                decrypted.append(mapping[char])
        result.append(''.join(decrypted))
    
    for line in result:
        print(line)

if __name__ == "__main__":
    main()
