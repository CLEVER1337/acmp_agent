
def main():
    with open('INPUT.TXT', 'r') as f:
        n = int(f.readline().strip())
        points = []
        for _ in range(n):
            x, y = map(int, f.readline().split())
            points.append((x, y))
    
    if n == 0:
        print(0)
        return
        
    points.sort()
    
    total_distance = 0
    current_x, current_y = 1, 1
    
    for i in range(n):
        target_x, target_y = points[i]
        
        if i == 0:
            total_distance += abs(target_x - current_x) + abs(target_y - current_y)
        else:
            prev_x, prev_y = points[i-1]
            total_distance += abs(target_x - prev_x) + abs(target_y - prev_y)
        
        current_x, current_y = target_x, target_y
    
    print(total_distance)

if __name__ == "__main__":
    main()
