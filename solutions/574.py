
def main():
    with open('INPUT.TXT', 'r') as f:
        s1 = f.readline().strip()
        s2 = f.readline().strip()
    
    if len(s1) != len(s2):
        with open('OUTPUT.TXT', 'w') as f:
            f.write('NO')
        return
    
    count = {}
    for char in s1:
        count[char] = count.get(char, 0) + 1
    
    for char in s2:
        if char not in count:
            with open('OUTPUT.TXT', 'w') as f:
                f.write('NO')
            return
        count[char] -= 1
        if count[char] < 0:
            with open('OUTPUT.TXT', 'w') as f:
                f.write('NO')
            return
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write('YES')

if __name__ == '__main__':
    main()
