
import sys

def is_runic_word(s):
    if not s:
        return "No"
    
    if not s[0].isupper():
        return "No"
    
    i = 0
    n = len(s)
    
    while i < n:
        # Определяем длину текущей руны (2, 3 или 4 буквы)
        remaining = n - i
        if remaining < 2:
            return "No"
            
        if remaining >= 4 and s[i+1].islower() and s[i+2].islower() and s[i+3].islower():
            rune_length = 4
        elif remaining >= 3 and s[i+1].islower() and s[i+2].islower():
            rune_length = 3
        elif remaining >= 2 and s[i+1].islower():
            rune_length = 2
        else:
            return "No"
        
        # Проверяем, что все буквы после первой в руне - строчные
        for j in range(i+1, i+rune_length):
            if not s[j].islower():
                return "No"
        
        i += rune_length
    
    return "Yes" if i == n else "No"

def main():
    with open('INPUT.TXT', 'r') as f:
        word = f.readline().strip()
    
    result = is_runic_word(word)
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(result)

if __name__ == "__main__":
    main()
