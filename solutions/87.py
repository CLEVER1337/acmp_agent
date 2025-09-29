
def main():
    strings = []
    with open('INPUT.TXT', 'r') as f:
        while True:
            line = f.readline().strip()
            if line == 'ENDOFINPUT':
                break
            if line:
                strings.append(line)
    
    string_set = set(strings)
    count = 0
    
    for s in strings:
        found = False
        for i in range(1, len(s)):
            prefix = s[:i]
            suffix = s[i:]
            if prefix in string_set and suffix in string_set:
                found = True
                break
        if found:
            count += 1
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(count))

if __name__ == '__main__':
    main()
