
def main():
    import sys
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    lines = data[1:1+n]
    
    key_phrase = "the quick brown fox jumps over the lazy dog"
    key_found = False
    mapping = {}
    
    for line in lines:
        if len(line) == len(key_phrase):
            if all(c1 == ' ' and c2 == ' ' or c1 != ' ' and c2 != ' ' 
                   for c1, c2 in zip(line, key_phrase)):
                temp_mapping = {}
                valid = True
                for c1, c2 in zip(line, key_phrase):
                    if c1 != ' ':
                        if c1 in temp_mapping:
                            if temp_mapping[c1] != c2:
                                valid = False
                                break
                        else:
                            temp_mapping[c1] = c2
                if valid and len(set(temp_mapping.values())) == len(temp_mapping):
                    mapping = temp_mapping
                    key_found = True
                    break
    
    if not key_found:
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
