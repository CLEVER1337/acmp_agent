
import sys
from collections import defaultdict

def main():
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    words = data[1:1+n]
    
    groups = defaultdict(list)
    
    for word in words:
        key = ''.join(sorted(word))
        groups[key].append(word)
    
    unique_groups = []
    for key, word_list in groups.items():
        unique_words = sorted(set(word_list))
        unique_groups.append((len(unique_words), unique_words))
    
    unique_groups.sort(key=lambda x: (-x[0], x[1][0]))
    
    output_lines = []
    for i in range(min(5, len(unique_groups))):
        count, word_list = unique_groups[i]
        output_lines.append(f"Группа {i+1}. Длина {count}")
        for word in word_list:
            output_lines.append(word)
        output_lines.append("")
    
    with open("OUTPUT.TXT", "w", encoding="utf-8") as f:
        f.write("\n".join(output_lines))

if __name__ == "__main__":
    main()
