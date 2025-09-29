
import math

def main():
    with open('INPUT.TXT', 'r') as f:
        data = f.read().split()
    
    k = int(data[0])
    T = int(data[1])
    mushrooms = []
    index = 2
    for i in range(k):
        x = int(data[index])
        y = int(data[index+1])
        r = int(data[index+2])
        index += 3
        mushrooms.append((x, y, r))
    
    min_time = T
    for i in range(k):
        for j in range(i + 1, k):
            x1, y1, r1 = mushrooms[i]
            x2, y2, r2 = mushrooms[j]
            distance = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
            initial_gap = distance - (r1 + r2)
            
            if initial_gap <= 0:
                min_time = 0
                break
            else:
                collision_time = initial_gap / 2.0
                if collision_time < min_time:
                    min_time = collision_time
            
        if min_time == 0:
            break
    
    result = min_time
    print("{:.2f}".format(result))

if __name__ == "__main__":
    main()
