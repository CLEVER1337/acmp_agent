
import sys

def main():
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    words = data[1:1+n]
    
    groups = {}
    for word in words:
        key = ''.join(sorted(word))
        if key not in groups:
            groups[key] = set()
        groups[key].add(word)
    
    result = []
    for key, word_set in groups.items():
        sorted_words = sorted(word_set)
        result.append((len(word_set), sorted_words))
    
    result.sort(key=lambda x: (-x[0], x[1][0]))
    
    output_lines = []
    for i in range(min(5, len(result))):
        count, word_list = result[i]
        sorted_group = sorted(word_list)
        output_lines.append(f"Group of size {count}: {' '.join(sorted_group)} .")
    
    sys.stdout.write("\n".join(output_lines))

if __name__ == "__main__":
    main()
