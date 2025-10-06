
import sys

def main():
    data = sys.stdin.read().splitlines()
    if not data:
        return
    
    first_line = data[0].strip()
    parts = first_line.split()
    name = parts[1]
    
    output_lines = []
    
    for i in range(1, len(data) - 1):
        line = data[i].strip()
        time_end = line.find(' ')
        if time_end == -1:
            continue
            
        text_part = line[time_end + 1:]
        if not text_part:
            continue
            
        last_char = text_part[-1]
        if last_char in '.!?':
            if last_char == '.':
                quoted_text = f'«{text_part[:-1]},»'
            else:
                quoted_text = f'«{text_part}»'
        else:
            quoted_text = f'«{text_part},»'
            
        speaker = "Fedya" if i % 2 == 1 else name
        output_lines.append(f"{quoted_text} --- skazal {speaker}.")
    
    for line in output_lines:
        print(line)

if __name__ == "__main__":
    main()
