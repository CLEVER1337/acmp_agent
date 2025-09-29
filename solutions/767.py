
def main():
    import sys
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    M = []
    for i in range(1, n+1):
        row = list(map(int, data[i].split()))
        M.append(row)
    
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if M[i][j] == 1:
                if M[j][i] == 1:
                    count += 1
    
    print(count)

if __name__ == "__main__":
    main()
