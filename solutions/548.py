
def main():
    with open('INPUT.TXT', 'r') as f:
        num1 = f.readline().strip()
        num2 = f.readline().strip()
    
    i, j = 0, 0
    result = []
    
    while i < len(num1) and j < len(num2):
        if num1[i:] < num2[j:]:
            result.append(num1[i])
            i += 1
        else:
            result.append(num2[j])
            j += 1
    
    while i < len(num1):
        result.append(num1[i])
        i += 1
        
    while j < len(num2):
        result.append(num2[j])
        j += 1
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(''.join(result))

if __name__ == '__main__':
    main()
