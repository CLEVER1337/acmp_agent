
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    k = int(data[1])
    p = int(data[2])
    moves = list(map(int, data[3:3+p]))
    
    winning_positions = set()
    for i in range(1, n+1):
        if i <= k:
            winning_positions.add(i)
        else:
            found = False
            for j in range(1, k+1):
                if i - j not in winning_positions:
                    found = True
                    break
            if found:
                winning_positions.add(i)
    
    results = []
    current_n = n
    for move in moves:
        if current_n <= k:
            if current_n == move:
                results.append('T')
            else:
                results.append('F')
            current_n -= move
        else:
            if current_n - move in winning_positions:
                results.append('F')
            else:
                results.append('T')
            current_n -= move
    
    for res in results:
        print(res)

if __name__ == "__main__":
    main()
