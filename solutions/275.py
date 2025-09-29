
def main():
    with open('INPUT.TXT', 'r') as f:
        n = int(f.readline().strip())
        numbers = [f.readline().strip() for _ in range(n)]
    
    results = []
    for binary_num in numbers:
        num = int(binary_num, 2)
        results.append("Yes" if num % 7 == 0 else "No")
    
    with open('OUTPUT.TXT', 'w') as f:
        for result in results:
            f.write(result + '\n')

if __name__ == "__main__":
    main()
