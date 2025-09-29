
def main():
    n = int(input().strip())
    if n == 1:
        print(0)
        return
        
    sequence = [0]
    for i in range(1, n):
        prev_digits = set(str(sequence[-1]))
        current = sequence[-1] + 1
        
        while True:
            current_digits = set(str(current))
            if not current_digits.intersection(prev_digits):
                sequence.append(current)
                break
            current += 1
            
    print(sequence[-1])

if __name__ == "__main__":
    main()
