
import sys

def is_runic_word(s):
    if not s:
        return "No"
    
    n = len(s)
    i = 0
    
    while i < n:
        # Первая буква руны должна быть заглавной
        if not s[i].isupper():
            return "No"
        
        # Определяем длину руны (2, 3 или 4 буквы)
        rune_length = 1
        
        # Считаем количество следующих строчных букв
        while i + rune_length < n and s[i + rune_length].islower():
            rune_length += 1
            if rune_length > 3:  # максимум 3 строчные буквы после заглавной
                break
        
        # Проверяем длину руны (должна быть от 2 до 4 символов)
        if rune_length < 2 or rune_length > 4:
            return "No"
        
        i += rune_length
    
    return "Yes" if i == n else "No"

def main():
    with open('INPUT.TXT', 'r') as f:
        word = f.readline().strip()
    
    result = is_runic_word(word)
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(result)

if __name__ == '__main__':
    main()
