
def main():
    with open('INPUT.TXT', 'r') as f:
        n = int(f.read().strip())
    
    if n <= 1:
        result = 0
    elif n == 2:
        result = 1
    elif n == 3:
        result = 2
    else:
        matches = n - 1
        if n > 3:
            matches += 1
        result = matches
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(result))

if __name__ == '__main__':
    main()
