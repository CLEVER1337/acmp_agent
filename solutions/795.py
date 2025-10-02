
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    sectors = list(map(int, data[1:1+n]))
    a = int(data[1+n])
    b = int(data[2+n])
    k = int(data[3+n])
    
    max_win = 0
    
    if k == 0:
        max_win = max(sectors)
    else:
        max_steps = (b + k - 1) // k
        min_steps = (a + k - 1) // k
        
        for steps in [min_steps, max_steps]:
            if steps == 0:
                idx = 0
            else:
                idx = steps % (2 * n)
                if idx >= n:
                    idx = 2 * n - idx
                else:
                    idx = idx % n
            
            max_win = max(max_win, sectors[idx])
            
        for steps in [min_steps - 1, max_steps - 1]:
            if steps < 0:
                continue
            idx = steps % (2 * n)
            if idx >= n:
                idx = 2 * n - idx
            else:
                idx = idx % n
            max_win = max(max_win, sectors[idx])
    
    print(max_win)

if __name__ == "__main__":
    main()
