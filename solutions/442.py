
def main():
    with open('INPUT.TXT', 'r') as f:
        data = f.read()
    
    stack = [10]
    current_size = 10
    char_count = {}
    i = 0
    n = len(data)
    
    while i < n:
        if data[i] == '<':
            j = i
            while j < n and data[j] != '>':
                j += 1
            if j < n:
                tag = data[i:j+1]
                if tag.startswith('<font'):
                    size_attr = ''
                    size_start = tag.find('size="')
                    if size_start != -1:
                        size_start += 6
                        size_end = tag.find('"', size_start)
                        if size_end != -1:
                            size_attr = tag[size_start:size_end]
                    
                    if size_attr:
                        if size_attr.startswith('+'):
                            try:
                                delta = int(size_attr[1:])
                                new_size = min(50, max(1, stack[-1] + delta))
                                stack.append(new_size)
                                current_size = new_size
                            except:
                                stack.append(stack[-1])
                                current_size = stack[-1]
                        elif size_attr.startswith('-'):
                            try:
                                delta = int(size_attr[1:])
                                new_size = min(50, max(1, stack[-1] - delta))
                                stack.append(new_size)
                                current_size = new_size
                            except:
                                stack.append(stack[-1])
                                current_size = stack[-1]
                        else:
                            try:
                                new_size = min(50, max(1, int(size_attr)))
                                stack.append(new_size)
                                current_size = new_size
                            except:
                                stack.append(stack[-1])
                                current_size = stack[-1]
                    else:
                        stack.append(stack[-1])
                        current_size = stack[-1]
                elif tag == '</font>':
                    if len(stack) > 1:
                        stack.pop()
                    current_size = stack[-1]
                i = j + 1
                continue
        elif data[i] not in ['\t', '\n', '\r', ' ']:
            if current_size not in char_count:
                char_count[current_size] = 0
            char_count[current_size] += 1
        
        i += 1
    
    with open('OUTPUT.TXT', 'w') as f:
        for size in sorted(char_count.keys()):
            f.write(f"{size} {char_count[size]}\n")

if __name__ == "__main__":
    main()
