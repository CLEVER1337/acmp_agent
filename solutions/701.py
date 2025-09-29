
def main():
    with open('INPUT.TXT', 'r') as f:
        data = f.readline().split()
    
    N = int(data[0])
    K_str = data[1]
    
    base = N % 10 + 2
    
    if base < 2:
        base = 2
    
    try:
        result = int(K_str, base)
    except:
        result = 0
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(result))

if __name__ == '__main__':
    main()
