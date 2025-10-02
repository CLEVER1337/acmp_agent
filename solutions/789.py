
def main():
    with open('INPUT.TXT', 'r') as f:
        n = int(f.read().strip())
    
    sequence = []
    num = 1
    
    while len(sequence) < n:
        digits = list(str(num))
        is_valid = True
        
        for i in range(len(digits) - 1):
            if digits[i] >= digits[i + 1]:
                is_valid = False
                break
                
        if is_valid:
            sequence.append(num)
            
        num += 1
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(sequence[-1]))

if __name__ == '__main__':
    main()
