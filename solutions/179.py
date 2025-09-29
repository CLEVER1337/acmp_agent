
def main():
    with open('INPUT.TXT', 'r') as f:
        k = int(f.read().strip())
    
    if k == 0:
        result = 1
    elif k == 1:
        result = 2
    else:
        a, b = 1, 2
        for _ in range(2, k + 1):
            a, b = b, a + b
        result = b
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(result))

if __name__ == '__main__':
    main()
