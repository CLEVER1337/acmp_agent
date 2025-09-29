
import math

def main():
    with open("input.txt", "r") as f:
        data = f.read().split()
    
    n = int(data[0])
    observer_x = float(data[1])
    observer_y = float(data[2])
    
    trees = []
    index = 3
    for i in range(n):
        x = float(data[index])
        y = float(data[index+1])
        r = float(data[index+2])
        index += 3
        trees.append((x, y, r))
    
    visible = True
    for x, y, r in trees:
        dx = observer_x - x
        dy = observer_y - y
        distance = math.sqrt(dx*dx + dy*dy)
        
        if distance <= r:
            visible = False
            break
    
    print("YES" if visible else "NO")

if __name__ == "__main__":
    main()
