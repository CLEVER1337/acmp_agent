
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    points = list(map(int, data[1:1+n]))
    
    min_ratio = float('inf')
    best_start = 0
    best_end = 0
    
    for i in range(n):
        for j in range(i+1, n):
            count = j - i + 1
            length = points[j] - points[i]
            ratio = length / count
            
            if ratio < min_ratio:
                min_ratio = ratio
                best_start = points[i]
                best_end = points[j]
    
    print(f"{best_start} {best_end}")

if __name__ == "__main__":
    main()
