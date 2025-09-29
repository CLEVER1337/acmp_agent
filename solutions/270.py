
import sys

def main():
    s = sys.stdin.readline().strip()
    if not s:
        print("Error!")
        return
        
    if '_' in s:
        # Проверяем на формат C++
        if s.startswith('_') or s.endswith('_'):
            print("Error!")
            return
            
        words = s.split('_')
        for word in words:
            if not word.islower() or not word.isalpha():
                print("Error!")
                return
                
        # Преобразуем C++ в Java
        result = words[0]
        for word in words[1:]:
            if word:
                result += word[0].upper() + word[1:]
        print(result)
        
    else:
        # Проверяем на формат Java
        if not s[0].islower():
            print("Error!")
            return
            
        # Преобразуем Java в C++
        result = []
        current_word = []
        
        for char in s:
            if char.isupper():
                if current_word:
                    result.append(''.join(current_word))
                    current_word = []
                current_word.append(char.lower())
            else:
                current_word.append(char)
                
        if current_word:
            result.append(''.join(current_word))
            
        print('_'.join(result))

if __name__ == "__main__":
    main()
