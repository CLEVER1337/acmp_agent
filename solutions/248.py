
import re

def process_year1(word):
    word = re.sub(r'ck', '', word)
    word = re.sub(r'ci', 'si', word)
    word = re.sub(r'ce', 'se', word)
    word = re.sub(r'c', 'k', word)
    return word

def process_year2(word):
    while True:
        original = word
        word = re.sub(r'ee', 'i', word)
        word = re.sub(r'oo', 'u', word)
        word = re.sub(r'([a-z])\1', r'\1', word)
        if word == original:
            break
    return word

def process_year3(word):
    if len(word) > 1 and word.endswith('e'):
        word = word[:-1]
    return word

def process_year4(text):
    words = text.split()
    result = []
    i = 0
    while i < len(words):
        if words[i] in ['a', 'an', 'the']:
            i += 1
        else:
            result.append(words[i])
            i += 1
    return ' '.join(result)

def process_word(word):
    if not word.isalpha():
        return word
    
    original_case = word[0].isupper()
    lower_word = word.lower()
    
    processed = process_year1(lower_word)
    processed = process_year2(processed)
    processed = process_year3(processed)
    
    if original_case and processed:
        processed = processed[0].upper() + processed[1:]
    
    return processed

def main():
    with open('INPUT.TXT', 'r', encoding='utf-8') as f:
        text = f.read().strip()
    
    words_and_punct = re.findall(r'\w+|[^\w\s]|\s+', text)
    
    processed_parts = []
    for part in words_and_punct:
        if part.isspace() or not part.isalnum():
            processed_parts.append(part)
        else:
            processed_parts.append(process_word(part))
    
    intermediate_text = ''.join(processed_parts)
    final_text = process_year4(intermediate_text)
    
    with open('OUTPUT.TXT', 'w', encoding='utf-8') as f:
        f.write(final_text)

if __name__ == '__main__':
    main()
