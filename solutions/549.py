
def main():
    with open('INPUT.TXT', 'r') as f:
        p, q = map(int, f.readline().split())
    
    n = 2
    result = []
    while p > 0:
        n += 1
        a = (p * n) // q
        result.append(a)
        p = p * n - a * q
        if p == 0:
            break
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(len(result) + 1) + '\n')
        for a in result:
            f.write(str(a) + '\n')

if __name__ == '__main__':
    main()
