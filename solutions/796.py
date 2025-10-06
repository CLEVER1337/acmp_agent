
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
        else:
            if current_para:
                paragraphs.append(' '.join(current_para))
                current_para = []
    
    if current_para:
        paragraphs.append(' '.join(current_para))
    
    output_lines = []
    indent = ' ' * b
    
    for para in paragraphs:
        words = []
        current_word = []
        in_word = False
        
        for char in para:
            if char.isalnum():
                if not in_word and current_word:
                    words.append(''.join(current_word))
                    current_word = []
                in_word = True
                current_word.append(char)
            elif char in [',', '.', '?', '!', '-', ':', "'"]:
                if in_word:
                    current_word.append(char)
                else:
                    if current_word:
                        words.append(''.join(current_word))
                    current_word = [char]
                in_word = False
            elif char == ' ':
                if in_word:
                    in_word = False
                if current_word:
                    words.append(''.join(current_word))
                    current_word = []
        
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

if __name__ == "__main__":
    main()
