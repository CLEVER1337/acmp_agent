
def main():
    with open("INPUT.TXT", "r") as f:
        n = int(f.readline().strip())
        m = int(f.readline().strip())
        coords = list(map(int, f.readline().split()))
    
    candles = []
    for i in range(0, len(coords), 2):
        candles.append((coords[i], coords[i+1]))
    
    if m == 0:
        print("YES")
        return
        
    # Проверяем вертикальные и горизонтальные разрезы
    for cut in range(1, n):
        left_count = 0
        right_count = 0
        for x, y in candles:
            if x < cut:
                left_count += 1
            elif x > cut:
                right_count += 1
        
        if left_count == 0 or right_count == 0:
            print("YES")
            return
            
        top_count = 0
        bottom_count = 0
        for x, y in candles:
            if y < cut:
                bottom_count += 1
            elif y > cut:
                top_count += 1
        
        if top_count == 0 or bottom_count == 0:
            print("YES")
            return
    
    print("NO")

if __name__ == "__main__":
    main()
