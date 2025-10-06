
import math

def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    c = int(data[1])
    p_val = int(data[2])
    index = 3
    
    houses = []
    for i in range(n):
        x = int(data[index])
        y = int(data[index+1])
        index += 2
        houses.append((x, y))
        
    xnet = int(data[index])
    ynet = int(data[index+1])
    
    total_length = 0.0
    for x, y in houses:
        dx = x - xnet
        dy = y - ynet
        distance = math.sqrt(dx*dx + dy*dy)
        total_length += distance
        
    total_cost = total_length * c
    
    if total_cost <= p_val:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
