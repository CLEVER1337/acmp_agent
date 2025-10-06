
def main():
    import sys
    data = sys.stdin.read().splitlines()
    n = int(data[0].strip())
    numbers = list(map(int, data[1].split()))
    
    unique_sorted = sorted(set(numbers))
    result = []
    i = 0
    while i < len(unique_sorted):
        start = unique_sorted[i]
        j = i
        while j < len(unique_sorted) - 1 and unique_sorted[j+1] == unique_sorted[j] + 1:
            j += 1
        end = unique_sorted[j]
        
        if end - start >= 2:
            result.append(f"<{start}, ..., {end}>")
        elif end - start == 1:
            result.append(str(start))
            result.append(str(end))
        else:
            result.append(str(start))
            
        i = j + 1
        
    print(", ".join(result))

if __name__ == "__main__":
    main()
