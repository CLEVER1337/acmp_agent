
def main():
    with open('INPUT.TXT', 'r') as f:
        n = int(f.readline().strip())
    
    if n < 5:
        print(0)
        return
        
    stones = [0] * (n + 1)
    moves = [0] * (n + 1)
    
    stones[1] = 0
    stones[2] = 0
    stones[3] = 0
    stones[4] = 0
    
    for i in range(5, n + 1):
        possible_moves = []
        for k in range(1, (i + 1) // 2):
            if k != i - k:
                if stones[k] == 0 or stones[i - k] == 0:
                    possible_moves.append(k)
        
        if possible_moves:
            stones[i] = 1
            moves[i] = min(possible_moves)
        else:
            stones[i] = 0
            moves[i] = 0
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(moves[n]))

if __name__ == '__main__':
    main()
