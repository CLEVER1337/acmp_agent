
def main():
    with open("INPUT.TXT", "r") as f:
        n = int(f.readline().strip())
        numbers = list(map(int, f.readline().split()))
    
    numbers = sorted(set(numbers))
    result = []
    i = 0
    
    while i < len(numbers):
        start = numbers[i]
        j = i
        while j < len(numbers) - 1 and numbers[j + 1] == numbers[j] + 1:
            j += 1
        
        if j > i:
            result.append(f"<{start}, ..., {numbers[j]}>")
        else:
            result.append(str(start))
        
        i = j + 1
    
    with open("OUTPUT.TXT", "w") as f:
        f.write(", ".join(result))

if __name__ == "__main__":
    main()
