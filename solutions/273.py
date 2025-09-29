
def main():
    with open('INPUT.TXT', 'r') as f:
        s = f.read().strip()
    
    seen = set()
    n = len(s)
    
    for i in range(n):
        if s[i] == '0':
            continue
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                num = s[i] + s[j] + s[k]
                seen.add(num)
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(len(seen)))

if __name__ == '__main__':
    main()
