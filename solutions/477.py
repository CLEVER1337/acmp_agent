
def main():
    with open('INPUT.TXT', 'r') as f:
        n_str = f.read().strip()
    
    if n_str == '0':
        print('2')
        return
        
    n = int(n_str)
    
    if n % 3 == 0:
        print('2')
    else:
        print('1')
        moves = []
        power = 0
        while True:
            move = 1 << power
            if move > n:
                break
            remaining = n - move
            if remaining % 3 == 0:
                moves.append(move)
            power += 1
        
        if moves:
            min_move = min(moves)
            print(str(min_move))
        else:
            print('1')

if __name__ == '__main__':
    main()
