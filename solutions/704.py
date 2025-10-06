
def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        print("NO")
        return
        
    n = int(data[0])
    m = int(data[1])
    candles = []
    index = 2
    for i in range(m):
        x = int(data[index])
        y = int(data[index+1])
        index += 2
        candles.append((x, y))
    
    if m == 0:
        print("YES")
        return
        
    possible = False
    
    for i in range(m):
        for j in range(i+1, m):
            x1, y1 = candles[i]
            x2, y2 = candles[j]
            dx = x2 - x1
            dy = y2 - y1
            
            if dx == 0 and dy == 0:
                continue
                
            if dx == 0:
                a = 1
                b = 0
                c = -x1
            elif dy == 0:
                a = 0
                b = 1
                c = -y1
            else:
                a = dy
                b = -dx
                c = dx * y1 - dy * x1
                
            all_on_same_side = True
            sign = None
            for cx, cy in candles:
                value = a * cx + b * cy + c
                if abs(value) < 1e-9:
                    all_on_same_side = False
                    break
                if sign is None:
                    sign = 1 if value > 0 else -1
                else:
                    if (value > 0 and sign < 0) or (value < 0 and sign > 0):
                        all_on_same_side = False
                        break
                        
            if all_on_same_side:
                possible = True
                break
                
        if possible:
            break
            
    if not possible:
        for test_x in [0.5, n-0.5]:
            all_on_same_side = True
            sign = None
            for cx, cy in candles:
                value = cx - test_x
                if abs(value) < 1e-9:
                    all_on_same_side = False
                    break
                if sign is None:
                    sign = 1 if value > 0 else -1
                else:
                    if (value > 0 and sign < 0) or (value < 0 and sign > 0):
                        all_on_same_side = False
                        break
            if all_on_same_side:
                possible = True
                break
                
        for test_y in [0.5, n-0.5]:
            all_on_same_side = True
            sign = None
            for cx, cy in candles:
                value = cy - test_y
                if abs(value) < 1e-9:
                    all_on_same_side = False
                    break
                if sign is None:
                    sign = 1 if value > 0 else -1
                else:
                    if (value > 0 and sign < 0) or (value < 0 and sign > 0):
                        all_on_same_side = False
                        break
            if all_on_same_side:
                possible = True
                break
                
    print("YES" if possible else "NO")

if __name__ == "__main__":
    main()
