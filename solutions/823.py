
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    points = []
    for i in range(n):
        x = int(data[2*i+1])
        y = int(data[2*i+2])
        points.append((x, y))
    
    if n == 0:
        print(0)
        return
        
    points.sort()
    min_x = min(p[0] for p in points)
    max_x = max(p[0] for p in points)
    
    dp_left = {}
    dp_right = {}
    
    layers = {}
    for x, y in points:
        if x not in layers:
            layers[x] = []
        layers[x].append(y)
    
    for x in layers:
        layers[x].sort()
    
    first_x = min_x
    min_layer = layers[first_x]
    start_min = min_layer[0]
    start_max = min_layer[-1]
    dp_left[first_x] = (start_max, start_max - start_min + start_max - start_min)
    dp_right[first_x] = (start_min, start_max - start_min)
    
    prev_x = first_x
    for x in sorted(layers.keys()):
        if x == first_x:
            continue
            
        current_layer = layers[x]
        min_y = current_layer[0]
        max_y = current_layer[-1]
        len_layer = max_y - min_y
        
        prev_left_y, prev_left_dist = dp_left[prev_x]
        prev_right_y, prev_right_dist = dp_right[prev_x]
        
        dist_left_from_left = prev_left_dist + abs(prev_left_y - max_y) + len_layer
        dist_left_from_right = prev_right_dist + abs(prev_right_y - max_y) + len_layer
        new_left_dist = min(dist_left_from_left, dist_left_from_right)
        dp_left[x] = (min_y, new_left_dist)
        
        dist_right_from_left = prev_left_dist + abs(prev_left_y - min_y) + len_layer
        dist_right_from_right = prev_right_dist + abs(prev_right_y - min_y) + len_layer
        new_right_dist = min(dist_right_from_left, dist_right_from_right)
        dp_right[x] = (max_y, new_right_dist)
        
        prev_x = x
        
    last_x = max_x
    result = min(dp_left[last_x][1], dp_right[last_x][1])
    print(result)

if __name__ == "__main__":
    main()
