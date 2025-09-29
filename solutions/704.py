
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
        x = float(data[index])
        y = float(data[index + 1])
        candles.append((x, y))
        index += 2
        
    if m == 0:
        print("YES")
        return
        
    center_x = n / 2.0
    center_y = n / 2.0
    
    for angle in range(0, 181):
        rad = angle * 3.141592653589793 / 180.0
        dx = -1.0 * (center_y * 2) * (-1 if angle > 90 else 1)
        dy = 0
        
        if angle == 0:
            line_normal = (1, 0)
            line_point = (center_x, 0)
        elif angle == 90:
            line_normal = (0, 1)
            line_point = (0, center_y)
        elif angle == 180:
            line_normal = (-1, 0)
            line_point = (center_x, 0)
        else:
            line_normal = (-1 * (center_y * 2) * (-1 if angle > 90 else 1), 0)
            line_normal = (1, 0)
            if angle != 0 and angle != 180:
                k = 1.0 / (3.141592653589793 - rad) if angle > 90 else 1.0 / rad
                line_normal = (1, -k)
                length = (line_normal[0]**2 + line_normal[1]**2)**0.5
                line_normal = (line_normal[0]/length, line_normal[1]/length)
                line_point = (center_x, center_y)
            else:
                line_normal = (1, 0)
                line_point = (center_x, 0)
                
        all_positive = True
        all_negative = True
        
        for x, y in candles:
            if angle == 0:
                value = x - center_x
            elif angle == 90:
                value = y - center_y
            elif angle == 180:
                value = center_x - x
            else:
                vec_x = x - line_point[0]
                vec_y = y - line_point[1]
                value = vec_x * line_normal[0] + vec_y * line_normal[1]
                
            if value > 1e-9:
                all_negative = False
            if value < -1e-9:
                all_positive = False
                
        if all_positive or all_negative:
            print("YES")
            return
            
    print("NO")

if __name__ == "__main__":
    main()
