
def main():
    mapping = {}
    with open('INPUT.TXT', 'r') as f:
        lines = f.readlines()
        
    punctuation = lines[0].strip()
    for i in range(1, 9):
        chars = lines[i].strip()
        button = str(i + 1)
        for idx, char in enumerate(chars):
            mapping[char] = (button, idx + 1)
    
    mapping[' '] = ('0', 1)
    for idx, char in enumerate(punctuation):
        mapping[char] = ('1', idx + 1)
    
    text = lines[9].strip()
    
    total_presses = 0
    current_case = 'upper'
    next_case = 'upper'
    
    for i, char in enumerate(text):
        if char.isalpha():
            if char.islower():
                needed_case = 'lower'
            else:
                needed_case = 'upper'
                
            if i == 0:
                current_case = 'upper'
            else:
                prev_char = text[i-1]
                if prev_char in '.!?' and current_case == 'lower':
                    next_case = 'upper'
                
            if needed_case != current_case:
                if needed_case == next_case:
                    total_presses += 1
                    current_case, next_case = next_case, 'lower'
                else:
                    total_presses += 1
                    current_case = needed_case
                    next_case = 'lower'
        
        button, presses = mapping[char.lower() if char.isalpha() else char]
        
        if i > 0:
            prev_char = text[i-1]
            if char != ' ' and prev_char != ' ':
                prev_button, _ = mapping[prev_char.lower() if prev_char.isalpha() else prev_char]
                if button == prev_button:
                    total_presses += 1
        
        total_presses += presses
        
        if char in '.!?' and current_case == 'lower':
            next_case = 'upper'
        elif char.isalpha():
            next_case = 'lower'
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(total_presses))

if __name__ == '__main__':
    main()
