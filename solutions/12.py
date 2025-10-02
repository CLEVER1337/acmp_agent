
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    index = 1
    count = 0
    
    for _ in range(n):
        X = int(data[index]); Y = int(data[index+1])
        points = []
        for i in range(8):
            points.append(int(data[index+2+i]))
        index += 10
        
        x_coords = [points[0], points[2], points[4], points[6]]
        y_coords = [points[1], points[3], points[5], points[7]]
        
        min_x = min(x_coords)
        max_x = max(x_coords)
        min_y = min(y_coords)
        max_y = max(y_coords)
        
        if min_x <= X <= max_x and min_y <= Y <= max_y:
            count += 1
            
    print(count)

if __name__ == "__main__":
    main()
