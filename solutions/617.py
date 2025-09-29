
import math

def main():
    with open('INPUT.TXT', 'r') as f:
        m, n, w, b = map(int, f.read().split())
    
    total = 0
    for i in range(w + 1):
        for j in range(b + 1):
            if i + j > min(m, n):
                continue
                
            ways_choose_rows = math.comb(m, i + j)
            ways_choose_cols = math.comb(n, i + j)
            ways_arrange_rooks = math.perm(i + j)
            
            ways_choose_white_positions = math.comb(i + j, i)
            
            ways = ways_choose_rows * ways_choose_cols * ways_arrange_rooks * ways_choose_white_positions
            
            total += ways
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(total))

if __name__ == '__main__':
    main()
