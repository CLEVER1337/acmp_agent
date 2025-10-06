
import sys

def main():
    data = sys.stdin.read().splitlines()
    if not data:
        return
    text = data[0]
    
    words = []
    current_word = []
    in_word = False
    
    for char in text:
        if char.isalpha():
            if not in_word:
                in_word = True
                current_word = []
            current_word.append(char)
        else:
            if in_word:
                words.append((''.join(current_word), False))
                in_word = False
            words.append((char, True))
    
    if in_word:
        words.append((''.join(current_word), False))
    
    def process_word(word):
        if not word:
            return word
            
        original_word = word
        word = word.lower()
        
        if word in ['a', 'an', 'the']:
            return ''
            
        chars = list(word)
        n = len(chars)
        
        i = 0
        while i < n:
            if chars[i] == 'c':
                if i + 1 < n and chars[i+1] == 'i':
                    chars[i] = 's'
                    del chars[i+1]
                    n -= 1
                elif i + 1 < n and chars[i+1] == 'e':
                    chars[i] = 's'
                    del chars[i+1]
                    n -= 1
                elif i + 1 < n and chars[i+1] == 'k':
                    del chars[i]
                    n -= 1
                    i -= 1
                else:
                    chars[i] = 'k'
            i += 1
        
        i = 0
        while i < n - 1:
            if chars[i] == chars[i+1]:
                if chars[i] == 'e':
                    chars[i] = 'i'
                    del chars[i+1]
                    n -= 1
                elif chars[i] == 'o':
                    chars[i] = 'u'
                    del chars[i+1]
                    n -= 1
                else:
                    del chars[i+1]
                    n -= 1
                continue
            i += 1
        
        if n > 1 and chars[-1] == 'e':
            chars.pop()
            n -= 1
        
        result = ''.join(chars)
        if original_word[0].isupper() and result:
            result = result[0].upper() + result[1:]
        return result
    
    output = []
    for item, is_punct in words:
        if is_punct:
            output.append(item)
        else:
            processed = process_word(item)
            if processed:
                output.append(processed)
    
    result_text = ''.join(output)
    print(result_text)

if __name__ == "__main__":
    main()
