
def main():
    with open('INPUT.TXT', 'r') as f:
        pattern = [line.strip() for line in f.readlines()]
    
    for i in range(3):
        for j in range(3):
            if (pattern[i][j] == pattern[i][j+1] == pattern[i+1][j] == pattern[i+1][j+1]):
                with open('OUTPUT.TXT', 'w') as f:
                    f.write('No')
                return
                
    with open('OUTPUT.TXT', 'w') as f:
        f.write('Yes')

if __name__ == '__main__':
    main()
