
import re

def main():
    with open('input.txt', 'r', encoding='utf-8') as f:
        lines = f.read().splitlines()
    
    if not lines:
        return
    
    first_line = lines[0]
    last_line = lines[-1]
    
    match = re.match(r'\d{2}:\d{2}:\d{2}: (\w+) signed on', first_line)
    if match:
        friend_name = match.group(1)
    
    output_lines = []
    
    for i, line in enumerate(lines[1:-1]):
        time_match = re.match(r'(\d{2}:\d{2}:\d{2}:) (.+)', line)
        if not time_match:
            continue
            
        content = time_match.group(2).strip()
        
        if content.endswith('.'):
            quoted_content = f'«{content[:-1]},»'
        elif content.endswith('!') or content.endswith('?'):
            quoted_content = f'«{content}»'
        else:
            quoted_content = f'«{content},»'
        
        speaker = "Fedya" if i % 2 == 0 else friend_name
        
        output_lines.append(f'{quoted_content} --- skazal {speaker}.')
    
    with open('OUTPUT.TXT', 'w', encoding='utf-8') as f:
        f.write('\n'.join(output_lines))

if __name__ == '__main__':
    main()
