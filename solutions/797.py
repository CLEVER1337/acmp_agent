
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    k = int(data[1])
    objects = []
    index = 2
    for i in range(n):
        x = int(data[index])
        y = int(data[index+1])
        index += 2
        objects.append((x, y))
    
    if k == 0:
        print(0)
        return
        
    objects.sort(key=lambda obj: (obj[1], obj[0]))
    
    min_days = 0
    current_y = 0
    current_x = 1
    
    for obj in objects:
        x, y = obj
        
        if y > current_y:
            min_days += y - current_y
            current_y = y
            current_x = 1
        
        if x < current_x:
            min_days += (current_x - x) * 2
            current_x = x
        elif x >= current_x + k:
            min_days += (x - (current_x + k - 1)) * 2
            current_x = x - k + 1
    
    print(min_days)

if __name__ == "__main__":
    main()
