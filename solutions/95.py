
def main():
    with open('INPUT.TXT', 'r') as f:
        n_str = f.read().strip()
    
    if len(n_str) == 0:
        result = 0
        operations = 0
    else:
        operations = 0
        current = n_str
        
        while len(current) > 1:
            total = sum(int(digit) for digit in current)
            current = str(total)
            operations += 1
        
        result = int(current)
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(f"{result} {operations}")

if __name__ == "__main__":
    main()
