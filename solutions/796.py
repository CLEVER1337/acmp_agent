
import sys

def main():
    data = sys.stdin.read().splitlines()
    if not data:
        return
    
    w, b = map(int, data[0].split())
    text_lines = data[1:]
    
    paragraphs = []
    current_para = []
    
    for line in text_lines:
        stripped = line.strip()
        if stripped:
            current_para.append(stripped)
        elif current_para:
            paragraphs.append(' '.join(current_para))
            current_para = []
    
    if current_para:
        paragraphs.append(' '.join(current_para))
    
    output_lines = []
    
    for para in paragraphs:
        words = []
        current_word = []
        in_word = False
        
        for char in para:
            if char.isalnum():
                if not in_word and current_word:
                    words.append(''.join(current_word))
                    current_word = []
                current_word.append(char)
                in_word = True
            elif char in [',', '.', '?', '!', '-', ':', "'"]:
                current_word.append(char)
                in_word = False
            elif char == ' ':
                if in_word or current_word:
                    words.append(''.join(current_word))
                    current_word = []
                in_word = False
        
        if current_word:
            words.append(''.join(current_word))
        
        current_line = ' ' * b
        first_in_para = True
        
        for word in words:
            if first_in_para:
                if len(current_line) + len(word) <= w:
                    current_line += word
                else:
                    output_lines.append(current_line.rstrip())
                    current_line = ' ' * b + word
                first_in_para = False
            else:
                if len(current_line) + 1 + len(word) <= w:
                    current_line += ' ' + word
                else:
                    output_lines.append(current_line.rstrip())
                    current_line = word
        
        if current_line.strip():
            output_lines.append(current_line.rstrip())
    
    with open('OUTPUT.TXT', 'w') as f:
        for line in output_lines:
            f.write(line + '\n')

if __name__ == '__main__':
    main()
