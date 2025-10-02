
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    k = int(data[1])
    p = int(data[2])
    moves = list(map(int, data[3:3+p]))
    
    results = []
    current_n = n
    
    for move in moves:
        if current_n == 0:
            results.append('F')
            continue
            
        if move > current_n:
            results.append('F')
            continue
            
        remaining = current_n - move
        
        if remaining == 0:
            results.append('T')
            current_n = 0
            continue
            
        win_positions = set()
        win_positions.add(0)
        
        for i in range(1, remaining + 1):
            can_win = False
            for take in range(1, k + 1):
                if take > i:
                    break
                if (i - take) not in win_positions:
                    can_win = True
                    break
            if not can_win:
                win_positions.add(i)
                
        if remaining in win_positions:
            results.append('F')
        else:
            results.append('T')
            
        current_n = remaining
        
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
