
def main():
    with open('INPUT.TXT', 'r') as f:
        n = f.readline().strip()
    
    target = n
    pos = 1
    current_num = 1
    
    while True:
        num_str = str(current_num)
        if num_str.startswith(target):
            break
        
        if len(num_str) > len(target):
            # Проверяем возможные пересечения между числами
            for i in range(1, len(target)):
                if num_str.endswith(target[:i]) and str(current_num + 1).startswith(target[i:]):
                    pos += len(num_str) - i
                    with open('OUTPUT.TXT', 'w') as f:
                        f.write(str(pos))
                    return
        
        pos += len(num_str)
        current_num += 1
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(pos))

if __name__ == '__main__':
    main()
