
def main():
    with open('INPUT.TXT', 'r') as f:
        s = f.readline().strip()
    
    n = len(s)
    max_num = ''
    
    for i in range(n - 1):
        if s[i] < s[i + 1]:
            max_num = s[:i] + s[i+1:]
            break
    else:
        max_num = s[:-1]
    
    max_num2 = ''
    for i in range(len(max_num) - 1):
        if max_num[i] < max_num[i + 1]:
            max_num2 = max_num[:i] + max_num[i+1:]
            break
    else:
        max_num2 = max_num[:-1]
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(max_num2)

if __name__ == '__main__':
    main()
