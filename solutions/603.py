
import sys

def main():
    data = sys.stdin.read().splitlines()
    if not data:
        return
    
    query = data[0].strip()
    text_lines = data[1:]
    
    if not query:
        print(''.join(text_lines), end='')
        return
        
    query_words = query.split()
    normalized_query = ' '.join(query_words).lower()
    
    full_text = ''.join(text_lines)
    
    result = []
    i = 0
    n = len(full_text)
    
    while i < n:
        if full_text[i].isspace():
            result.append(full_text[i])
            i += 1
            continue
            
        start = i
        words_found = []
        current_word = []
        j = i
        
        while j < n and len(words_found) < len(query_words):
            if not full_text[j].isspace():
                current_word.append(full_text[j])
                j += 1
            else:
                if current_word:
                    words_found.append(''.join(current_word))
                    current_word = []
                j += 1
                while j < n and full_text[j].isspace():
                    j += 1
        
        if current_word and len(words_found) < len(query_words):
            words_found.append(''.join(current_word))
            
        if len(words_found) == len(query_words):
            candidate = ' '.join(words_found).lower()
            if candidate == normalized_query:
                result.append('@')
                
        result.append(full_text[i])
        i += 1
        
    print(''.join(result), end='')

if __name__ == "__main__":
    main()
