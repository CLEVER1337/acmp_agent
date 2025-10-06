
def main():
    import sys
    data = sys.stdin.read().splitlines()
    if not data:
        print("NO")
        return
        
    n, m = map(int, data[0].split())
    ad_lines = data[1:1+n]
    screen_lines = data[1+n:1+2*n]
    
    color_map = {
        'R': 1,
        'G': 2,
        'B': 4,
        '.': 0
    }
    
    for i in range(n):
        ad_row = ad_lines[i].strip()
        screen_row = list(map(int, screen_lines[i].split()))
        
        for j in range(m):
            ad_color = ad_row[j]
            required = color_map[ad_color]
            available = screen_row[j]
            
            if required == 0:
                continue
                
            if (available & required) == 0:
                print("NO")
                return
                
    print("YES")

if __name__ == "__main__":
    main()
