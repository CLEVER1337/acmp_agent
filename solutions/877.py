
import re

def main():
    with open('input.txt', 'r', encoding='utf-8') as f:
        lines = f.read().splitlines()
    
    if not lines:
        return
    
    first_line = lines[0]
    signed_on_match = re.search(r'(\d{2}:\d{2}:\d{2}): (.+) signed on', first_line)
    if not signed_on_match:
        return
        
    friend_name = signed_on_match.group(2)
    
    output_lines = []
    
    for i, line in enumerate(lines[1:-1]):
        time_match = re.match(r'(\d{2}:\d{2}:\d{2}): (.+)', line)
        if not time_match:
            continue
            
        content = time_match.group(2).strip()
        
        if not content:
            continue
            
        last_char = content[-1]
        if last_char == '.':
            quoted_content = f'«{content[:-1]},»'
        else:
            quoted_content = f'«{content}»'
        
        speaker = 'Fedya' if i % 2 == 0 else friend_name
        
        output_lines.append(f'{quoted_content} --- skazal {speaker}.')
    
    with open('OUTPUT.TXT', 'w', encoding='utf-8') as f:
        f.write('\n'.join(output_lines))

if __name__ == '__main__':
    main()
