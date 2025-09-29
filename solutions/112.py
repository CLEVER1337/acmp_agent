
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    k = int(data[1])
    index = 2
    total_pushups = 0
    
    for _ in range(k):
        row = list(map(int, data[index:index+n]))
        index += n
        
        count = 0
        for i in range(1, n):
            key = row[i]
            j = i - 1
            while j >= 0 and row[j] > key:
                count += 1
                row[j + 1] = row[j]
                j -= 1
            row[j + 1] = key
            
        total_pushups += count
    
    print(total_pushups)

if __name__ == "__main__":
    main()
