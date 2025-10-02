
def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        print("0.000")
        return
        
    n = int(data[0])
    ships = []
    index = 1
    for i in range(n):
        x = int(data[index])
        y = int(data[index+1])
        s = int(data[index+2])
        index += 3
        ships.append((x, y, s))
    
    if n == 0:
        print("0.000")
        return
        
    min_x = float('-inf')
    max_x = float('inf')
    min_y = float('-inf')
    max_y = float('inf')
    
    for x, y, s in ships:
        ship_min_x = x - s
        ship_max_x = x
        ship_min_y = y - s
        ship_max_y = y
        
        min_x = max(min_x, ship_min_x)
        max_x = min(max_x, ship_max_x)
        min_y = max(min_y, ship_min_y)
        max_y = min(max_y, ship_max_y)
    
    if min_x > max_x or min_y > max_y:
        area = 0.0
    else:
        width = max_x - min_x
        height = max_y - min_y
        area = width * height
        
    print("{:.3f}".format(area))

if __name__ == "__main__":
    main()
