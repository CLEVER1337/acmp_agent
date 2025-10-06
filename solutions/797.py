
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
    
    if k >= 50:
        print(0)
        return
        
    max_y = max(obj[1] for obj in objects)
    min_y = min(obj[1] for obj in objects)
    
    columns = {}
    for obj in objects:
        x, y = obj
        if x not in columns:
            columns[x] = []
        columns[x].append(y)
    
    for x in columns:
        columns[x].sort()
    
    x_coords = sorted(columns.keys())
    min_days = float('inf')
    
    for start_x in range(1, 51 - k + 1):
        end_x = start_x + k - 1
        days = 0
        current_y = 1
        
        while current_y <= 50:
            found_in_row = False
            for x in x_coords:
                if start_x <= x <= end_x:
                    for y in columns[x]:
                        if current_y <= y < current_y + k:
                            found_in_row = True
                            break
                    if found_in_row:
                        break
            
            if found_in_row:
                days += 1
                current_y += k
            else:
                current_y += 1
        
        min_days = min(min_days, days - 1 + (end_x - start_x))
    
    print(min_days)

if __name__ == "__main__":
    main()
