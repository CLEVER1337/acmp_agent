
import re

def main():
    with open('INPUT.TXT', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    if not lines:
        return
    
    query = lines[0].strip()
    text_lines = lines[1:]
    
    # Получаем слова из запроса
    query_words = query.split()
    query_pattern = r'\s+'.join(re.escape(word) for word in query_words)
    
    # Читаем весь текст
    full_text = ''.join(text_lines)
    
    # Находим все вхождения
    matches = []
    for match in re.finditer(query_pattern, full_text, re.IGNORECASE):
        matches.append(match.start())
    
    # Строим результат с символами @
    result = []
    current_pos = 0
    
    for match_pos in sorted(matches):
        # Добавляем текст до вхождения
        result.append(full_text[current_pos:match_pos])
        # Добавляем символ @
        result.append('@')
        # Добавляем само вхождение
        result.append(full_text[match_pos:match_pos + len(query.replace(' ', '')) + (len(query_words) - 1)])
        current_pos = match_pos + len(query.replace(' ', '')) + (len(query_words) - 1)
    
    # Добавляем оставшийся текст
    result.append(full_text[current_pos:])
    
    with open('OUTPUT.TXT', 'w', encoding='utf-8') as f:
        f.write(''.join(result))

if __name__ == '__main__':
    main()
