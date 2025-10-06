
def main():
    mapping = {}
    for i in range(1, 10):
        line = input().strip()
        for idx, char in enumerate(line):
            mapping[char] = (str(i), idx + 1)
    mapping[' '] = ('0', 1)
    
    text = input().strip()
    
    caps_mode = True
    total_presses = 0
    prev_button = None
    
    for i, char in enumerate(text):
        if char in mapping:
            button, presses = mapping[char]
        else:
            continue
            
        if char.isalpha():
            if char.isupper() and not caps_mode:
                total_presses += 1
                caps_mode = True
            elif char.islower() and caps_mode:
                total_presses += 1
                caps_mode = False
                
        if button == prev_button and char != ' ':
            total_presses += 1
            
        total_presses += presses
        prev_button = button
        
        if char in '.!?' and not caps_mode:
            caps_mode = True
            
    print(total_presses)

if __name__ == "__main__":
    main()
