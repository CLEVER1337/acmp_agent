
def main():
    import sys
    data = sys.stdin.read().split()
    K = int(data[0])
    p1 = int(data[1])
    p2 = int(data[2])
    p3 = int(data[3])
    
    if p1 == 100 and p2 == 0:
        print(0)
        return
        
    if p1 == 0 and p2 == 100:
        print(0)
        return
        
    p1_val = p1 / 100.0
    p2_val = p2 / 100.0
    p3_val = p3 / 100.0
    
    E_chess_win = p1_val
    E_chess_draw = p3_val * 0.5
    E_chess_total = E_chess_win + E_chess_draw
    
    E_volleyball = (1 - p2_val)
    
    diff_per_game = abs(E_chess_total - E_volleyball)
    
    if diff_per_game == 0:
        print(0)
        return
        
    total_diff = diff_per_game * K
    
    if total_diff == 0:
        print(0)
        return
        
    min_chess = int(total_diff / diff_per_game)
    
    if min_chess > K:
        min_chess = K
        
    print(min_chess)

if __name__ == "__main__":
    main()
