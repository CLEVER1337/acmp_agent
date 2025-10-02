
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    directions = list(map(int, data[1:1+n]))
    
    if n < 3:
        print(0)
        return
        
    sides = []
    current_side = 0
    for d in directions:
        if d == 1:
            current_side += 1
        else:
            if current_side > 0:
                sides.append(current_side)
                current_side = 0
    if current_side > 0:
        sides.append(current_side)
    
    total = 0
    for side_length in sides:
        if side_length >= 2:
            total += (side_length - 1) * (side_length) // 2
            
    print(total)

if __name__ == "__main__":
    main()
