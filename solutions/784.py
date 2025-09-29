
def main():
    with open('INPUT.TXT', 'r') as f:
        n = int(f.readline().strip())
        a = int(f.readline().strip())
        b = int(f.readline().strip())
    
    while a != b:
        if a > b:
            a //= 2
        else:
            b //= 2
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(a))

if __name__ == '__main__':
    main()
