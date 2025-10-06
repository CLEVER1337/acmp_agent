
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    sectors = list(map(int, data[1:1+n]))
    a = int(data[1+n])
    b = int(data[2+n])
    k = int(data[3+n])
    
    max_win = 0
    total_sectors = n
    
    if k == 0:
        print(max(sectors))
        return
        
    for speed in [a, b]:
        if speed < k:
            rotations = 0
        else:
            rotations = (speed - 1) // k
            
        steps = rotations % total_sectors
        forward_index = steps
        backward_index = (total_sectors - steps) % total_sectors
        
        candidate1 = sectors[forward_index]
        candidate2 = sectors[backward_index]
        current_max = max(candidate1, candidate2)
        if current_max > max_win:
            max_win = current_max
            
    mid_speed = (a + b) // 2
    if a <= mid_speed <= b:
        if mid_speed < k:
            rotations = 0
        else:
            rotations = (mid_speed - 1) // k
            
        steps = rotations % total_sectors
        forward_index = steps
        backward_index = (total_sectors - steps) % total_sectors
        
        candidate1 = sectors[forward_index]
        candidate2 = sectors[backward_index]
        current_max = max(candidate1, candidate2)
        if current_max > max_win:
            max_win = current_max
            
    print(max_win)

if __name__ == "__main__":
    main()
