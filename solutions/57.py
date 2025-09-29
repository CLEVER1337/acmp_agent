
import math

def main():
    with open("INPUT.TXT", "r") as f:
        data = f.read().splitlines()
    
    n, c, p = map(int, data[0].split())
    houses = []
    for i in range(1, 1 + n):
        x, y = map(int, data[i].split())
        houses.append((x, y))
    
    xnet, ynet = map(int, data[1 + n].split())
    
    total_length = 0.0
    for x, y in houses:
        dx = x - xnet
        dy = y - ynet
        distance = math.sqrt(dx*dx + dy*dy)
        total_length += distance
    
    total_cost = total_length * c
    
    if total_cost <= p:
        with open("OUTPUT.TXT", "w") as f:
            f.write("YES")
    else:
        with open("OUTPUT.TXT", "w") as f:
            f.write("NO")

if __name__ == "__main__":
    main()
