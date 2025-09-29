
def main():
    with open('INPUT.TXT', 'r') as f:
        n = int(f.read().strip())
    
    if n == 0:
        with open('OUTPUT.TXT', 'w') as f:
            f.write('0')
        return
    
    binary = bin(n)[2:]
    rotations = []
    current = binary
    
    for _ in range(len(binary)):
        rotations.append(current)
        current = current[-1] + current[:-1]
    
    max_binary = max(rotations)
    result = int(max_binary, 2)
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(result))

if __name__ == '__main__':
    main()
