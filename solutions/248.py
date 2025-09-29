
import re

def process_year1(word):
    i = 0
    result = []
    n = len(word)
    
    while i < n:
        if word[i] == 'c':
            if i + 1 < n:
                if word[i+1] in 'ie':
                    result.append('s')
                    i += 1
                elif word[i+1] == 'k':
                    result.append('')
                    i += 1
                else:
                    result.append('k')
            else:
                result.append('k')
            i += 1
        else:
            result.append(word[i])
            i += 1
            
    return ''.join(result)

def process_year2(word):
    i = 0
    result = []
    n = len(word)
    
    while i < n:
        if i + 1 < n and word[i] == word[i+1]:
            if word[i] == 'e':
                result.append('i')
                i += 2
            elif word[i] == 'o':
                result.append('u')
                i += 2
            else:
                result.append(word[i])
                i += 1
        else:
            result.append(word[i])
            i += 1
            
    return ''.join(result)

def process_year3(word):
    if len(word) > 1 and word.endswith('e'):
        return word[:-1]
    return word

def process_word(word):
    if not word:
        return word
    
    original_word = word
    is_capital = word[0].isupper()
    word_lower = word.lower()
    
    if word_lower in ['a', 'an', 'the']:
        return ''
    
    processed = process_year1(word_lower)
    processed = process_year2(processed)
    processed = process_year3(processed)
    
    if is_capital and processed:
        processed = processed[0].upper() + processed[1:]
    
    return processed

def main():
    with open('INPUT.TXT', 'r', encoding='utf-8') as f:
        text = f.read().strip()
    
    pattern = r'([a-zA-Z]+|[^a-zA-Z\s]+)'
    tokens = re.findall(pattern, text)
    
    result_tokens = []
    for token in tokens:
        if token.isalpha():
            processed = process_word(token)
            if processed:
                result_tokens.append(processed)
        else:
            result_tokens.append(token)
    
    result = ''.join(result_tokens)
    
    with open('OUTPUT.TXT', 'w', encoding='utf-8') as f:
        f.write(result)

if __name__ == '__main__':
    main()
