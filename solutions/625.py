
def main():
    mapping = {}
    with open("INPUT.TXT", "r") as f:
        lines = f.readlines()
        
        # Читаем символы для кнопок 1-9
        for i in range(9):
            button_chars = lines[i].strip()
            for j, char in enumerate(button_chars):
                mapping[char] = (str(i + 1), j + 1)
        
        text = lines[9].strip()
    
    total_presses = 0
    current_case = "upper"  # Начинаем с режима "первой заглавной буквы"
    prev_button = None
    
    i = 0
    while i < len(text):
        char = text[i]
        
        if char == ' ':
            total_presses += 1
            prev_button = '0'
            i += 1
            continue
        
        if char in mapping:
            button, presses_needed = mapping[char]
            required_case = "upper" if char.isupper() else "lower"
            
            # Проверяем, нужно ли менять регистр
            if current_case != required_case:
                total_presses += 1  # Нажатие '#'
                current_case = required_case
            
            # Если предыдущий символ был на той же кнопке и не пробел
            if prev_button == button:
                total_presses += 1  # Нажатие для перемещения курсора
            
            total_presses += presses_needed
            prev_button = button
            
            # Проверяем, активируется ли режим "первой заглавной буквы"
            if char in ['.', '!', '?'] and current_case == "lower":
                current_case = "upper"
            
            i += 1
        else:
            # Обработка специальных символов (должны быть в mapping по условию)
            i += 1
    
    with open("OUTPUT.TXT", "w") as f:
        f.write(str(total_presses))

if __name__ == "__main__":
    main()
