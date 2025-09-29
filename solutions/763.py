
def main():
    with open("INPUT.TXT", "r") as f:
        x, y = map(int, f.readline().split())
    
    if x == 1 and y == 1:
        print(0)
        return
        
    def is_winning_position(a, b):
        if a == 1 and b == 1:
            return False
            
        moves = []
        if a > 1:
            moves.append((1, b))
        if b > 1:
            moves.append((a, 1))
            
        for move in moves:
            if not is_winning_position(*move):
                return True
                
        return False
        
    if is_winning_position(x, y):
        print(1)
    else:
        print(2)

if __name__ == "__main__":
    main()
