
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
    indent = ' ' * b
    
    for para in paragraphs:
        words = []
        current_word = []
        
        for char in para:
            if char == ' ':
                if current_word:
                    words.append(''.join(current_word))
                    current_word = []
            elif char in ',.?!-:\'':
                if current_word:
                    current_word.append(char)
                else:
                    words.append(char)
            else:
                current_word.append(char)
        
        if current_word:
            words.append(''.join(current_word))
        
        if not words:
            continue
            
        current_line = indent
        first_word = True
        
        for word in words:
            if first_word:
                if len(current_line) + len(word) <= w:
                    current_line += word
                    first_word = False
                else:
                    output_lines.append(current_line.rstrip())
                    current_line = indent + word
            else:
                if len(current_line) + 1 + len(word) <= w:
                    current_line += ' ' + word
                else:
                    output_lines.append(current_line.rstrip())
                    current_line = indent + word
        
        if current_line != indent:
            output_lines.append(current_line.rstrip())
    
    for line in output_lines:
        print(line)

if __name__ == '__main__':
    main()
