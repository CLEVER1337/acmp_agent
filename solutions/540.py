
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    m = int(data[1])
    r = int(data[2])
    first_row = list(map(int, data[3:3+m]))
    
    if n == 1:
        print(" ".join(map(str, first_row)))
        return
        
    row = first_row[:]
    for i in range(1, n):
        new_row = [0] * m
        prefix = [0] * (m + 1)
        for j in range(m):
            prefix[j+1] = (prefix[j] + row[j]) % r
            
        for j in range(m):
            new_row[j] = prefix[j+1] % r
            
        row = new_row
        
    print(" ".join(map(str, row)))

if __name__ == "__main__":
    main()
