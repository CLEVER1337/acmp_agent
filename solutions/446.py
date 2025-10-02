
def main():
    import sys
    data = sys.stdin.read().splitlines()
    n, m = map(int, data[0].split())
    
    ad = []
    for i in range(1, 1 + n):
        ad.append(data[i].strip())
    
    screen = []
    for i in range(1 + n, 1 + n + n):
        row = list(map(int, data[i].split()))
        screen.append(row)
    
    color_map = {
        '.': 0,
        'R': 1,
        'G': 2,
        'B': 4
    }
    
    for i in range(n):
        for j in range(m):
            ad_color = ad[i][j]
            screen_capabilities = screen[i][j]
            
            if ad_color == '.':
                continue
                
            required_color = color_map[ad_color]
            if (screen_capabilities & required_color) == 0:
                print("NO")
                return
                
    print("YES")

if __name__ == "__main__":
    main()
