
def main():
    n = int(input().strip())
    if n == 1:
        print(0)
        return
        
    a = [0]
    for i in range(1, n):
        prev_digits = set(str(a[-1]))
        current = a[-1] + 1
        while True:
            current_digits = set(str(current))
            if not current_digits.intersection(prev_digits):
                break
            current += 1
        a.append(current)
    
    print(a[-1])

if __name__ == "__main__":
    main()
