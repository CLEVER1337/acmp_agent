
def main():
    with open('INPUT.TXT', 'r') as f:
        s = int(f.read().strip())
    
    result = []
    while s > 0:
        result.append(str(s))
        if s == 1:
            break
        layer = 1
        total = 1
        while total < s:
            layer += 1
            total += layer
        pos_in_layer = s - (total - layer)
        if pos_in_layer % 2 == 1:
            s = total - layer + (pos_in_layer + 1) // 2
        else:
            s = total - layer + layer + (pos_in_layer // 2)
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(' '.join(result))

if __name__ == '__main__':
    main()
