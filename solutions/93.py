
def main():
    with open('INPUT.TXT', 'r') as f:
        n = int(f.readline().strip())
        gods = [f.readline().strip() for _ in range(n)]
        m = int(f.readline().strip())
        words = [f.readline().strip() for _ in range(m)]
    
    result = []
    for god in gods:
        count = 0
        for word in words:
            if len(god) != len(word):
                continue
            errors = 0
            for i in range(len(god)):
                if god[i] != word[i]:
                    errors += 1
                    if errors > 1:
                        break
            if errors == 1:
                count += 1
        result.append(str(count))
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(' '.join(result))

if __name__ == '__main__':
    main()
