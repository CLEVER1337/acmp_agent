
def main():
    with open('INPUT.TXT', 'r') as f:
        S = f.readline().strip()
        T = f.readline().strip()
    
    n = len(S)
    m = len(T)
    
    if m == 0 or n < m:
        with open('OUTPUT.TXT', 'w') as f:
            f.write('')
        return
    
    result = []
    i = 0
    while i <= n - m:
        pos = S.find(T, i)
        if pos == -1:
            break
        result.append(str(pos))
        i = pos + 1
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(' '.join(result))

if __name__ == '__main__':
    main()
