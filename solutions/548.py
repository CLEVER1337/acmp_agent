
def main():
    with open('INPUT.TXT', 'r') as f:
        a = f.readline().strip()
        b = f.readline().strip()
    
    result = []
    i = j = 0
    
    while i < len(a) and j < len(b):
        if a[i:] < b[j:]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    
    while i < len(a):
        result.append(a[i])
        i += 1
        
    while j < len(b):
        result.append(b[j])
        j += 1
        
    with open('OUTPUT.TXT', 'w') as f:
        f.write(''.join(result))

if __name__ == '__main__':
    main()
