
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    k = int(data[1])
    p = int(data[2])
    moves = list(map(int, data[3:3+p]))
    
    results = []
    current = n
    
    for move in moves:
        remainder = current % (k + 1)
        
        if remainder == 0:
            correct_move = k
        else:
            correct_move = remainder
            
        if move == correct_move:
            results.append('T')
        else:
            results.append('F')
            
        current -= move
        
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
