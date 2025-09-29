
def main():
    with open('INPUT.TXT', 'r') as f:
        n = int(f.readline().strip())
        operations = []
        for _ in range(n):
            line = f.readline().split()
            operations.append(line)
    
    shelf = []
    output = []
    
    for op in operations:
        if len(op) == 2:
            action, value = op
            if action == '1':
                shelf.insert(0, int(value))
            elif action == '2':
                shelf.append(int(value))
        else:
            action = op[0]
            if action == '3':
                output.append(str(shelf.pop(0)))
            elif action == '4':
                output.append(str(shelf.pop()))
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write('\n'.join(output))

if __name__ == '__main__':
    main()
