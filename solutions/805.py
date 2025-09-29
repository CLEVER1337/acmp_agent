
def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
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
    
    min_x = float('-inf')
    max_x = float('inf')
    min_y = float('-inf')
    max_y = float('inf')
    
    for x, y, s in ships:
        x1 = x
        y1 = y
        x2 = x - s
        y2 = y
        x3 = x
        y3 = y - s
        
        left_bound = x - s
        right_bound = x
        bottom_bound = y - s
        top_bound = y
        
        min_x = max(min_x, left_bound)
        max_x = min(max_x, right_bound)
        min_y = max(min_y, bottom_bound)
        max_y = min(max_y, top_bound)
    
    if min_x > max_x or min_y > max_y:
        area = 0.0
    else:
        width = max_x - min_x
        height = max_y - min_y
        area = width * height
    
    print("{:.3f}".format(area))

if __name__ == "__main__":
    main()
