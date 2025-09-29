
def main():
    with open('INPUT.TXT', 'r') as f:
        n = int(f.read().strip())
    
    count = 0
    num = 6
    
    while count < n:
        num += 1
        binary = bin(num)[2:]
        if binary.count('1') == 3:
            count += 1
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(num))

if __name__ == '__main__':
    main()
