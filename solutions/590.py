
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    points = []
    index = 1
    for i in range(n):
        x = int(data[index])
        y = int(data[index+1])
        z = int(data[index+2])
        index += 3
        points.append((x, y, z))
    
    if n == 0:
        print("Yes")
        return
        
    center_x = sum(p[0] for p in points) / n
    center_y = sum(p[1] for p in points) / n
    center_z = sum(p[2] for p in points) / n
    
    symmetric_points = set()
    for p in points:
        sym_x = 2 * center_x - p[0]
        sym_y = 2 * center_y - p[1]
        sym_z = 2 * center_z - p[2]
        symmetric_points.add((sym_x, sym_y, sym_z))
    
    for p in points:
        if (p[0], p[1], p[2]) not in symmetric_points:
            print("No")
            return
            
    print("Yes")

if __name__ == "__main__":
    main()
