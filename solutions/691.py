
def main():
    allowed_letters = set('ABCEHKMOPTXY')
    with open('INPUT.TXT', 'r') as f:
        n = int(f.readline().strip())
        lines = [line.strip() for line in f.readlines()]
    
    results = []
    for line in lines:
        if len(line) != 6:
            results.append('No')
            continue
        
        if (line[0] in allowed_letters and 
            line[1].isdigit() and 
            line[2].isdigit() and 
            line[3].isdigit() and 
            line[4] in allowed_letters and 
            line[5] in allowed_letters):
            results.append('Yes')
        else:
            results.append('No')
    
    with open('OUTPUT.TXT', 'w') as f:
        for result in results:
            f.write(result + '\n')

if __name__ == '__main__':
    main()
