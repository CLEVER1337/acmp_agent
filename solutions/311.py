
def main():
    with open('INPUT.TXT', 'r') as f:
        n = int(f.read().strip())
    
    total_sum = 0
    current_factorial = 1
    
    for i in range(1, n + 1):
        current_factorial *= i
        total_sum += current_factorial
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(total_sum))

if __name__ == '__main__':
    main()
