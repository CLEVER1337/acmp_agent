
def main():
    with open("INPUT.TXT", "r") as f:
        n = int(f.readline().strip())
        numbers = []
        for _ in range(n):
            numbers.append(int(f.readline().strip()))
    
    numbers.sort()
    
    current_sum = 0
    for num in numbers:
        if num > current_sum + 1:
            break
        current_sum += num
    
    result = current_sum + 1
    
    with open("OUTPUT.TXT", "w") as f:
        f.write(str(result))

if __name__ == "__main__":
    main()
