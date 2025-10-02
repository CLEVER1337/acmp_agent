
import math

def main():
    with open('INPUT.TXT', 'r') as f:
        data = f.read().split()
    
    n = int(data[0])
    c = int(data[1])
    p = int(data[2])
    
    coords = []
    index = 3
    for i in range(n):
        x = int(data[index])
        y = int(data[index + 1])
        coords.append((x, y))
        index += 2
    
    xnet = int(data[index])
    ynet = int(data[index + 1])
    
    total_length = 0.0
    for x, y in coords:
        distance = math.sqrt((x - xnet)**2 + (y - ynet)**2)
        total_length += distance
    
    total_cost = total_length * c
    
    if total_cost <= p:
        with open('OUTPUT.TXT', 'w') as f:
            f.write('YES')
    else:
        with open('OUTPUT.TXT', 'w') as f:
            f.write('NO')

if __name__ == '__main__':
    main()
