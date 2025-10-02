
import math

def main():
    with open("INPUT.TXT", "r") as f:
        m, n, w, b = map(int, f.read().split())
    
    total = 0
    for i in range(w, min(m, n) + 1):
        for j in range(b, min(m, n) + 1):
            if i + j > min(m, n):
                continue
                
            ways_rows = math.comb(m, i) * math.comb(m - i, j)
            ways_cols = math.comb(n, i) * math.comb(n - i, j)
            
            ways_white = math.comb(n, i) * math.comb(m, i) * math.factorial(i)
            ways_black = math.comb(n - i, j) * math.comb(m - i, j) * math.factorial(j)
            
            total += ways_white * ways_black
    
    with open("OUTPUT.TXT", "w") as f:
        f.write(str(total))

if __name__ == "__main__":
    main()
