
def main():
    with open("INPUT.TXT", "r") as f:
        data = f.read().split()
    
    L = int(data[0])
    N = int(data[1])
    numbers = list(map(int, data[2:2+N]))
    
    numbers.sort()
    
    min_count = N
    for i in range(N):
        count = 1
        current_max = numbers[i] + L
        
        for j in range(i + 1, N):
            if numbers[j] - L > current_max:
                count += 1
                current_max = numbers[j] + L
            else:
                current_max = min(current_max, numbers[j] + L)
        
        min_count = min(min_count, count)
    
    with open("OUTPUT.TXT", "w") as f:
        f.write(str(min_count))

if __name__ == "__main__":
    main()
