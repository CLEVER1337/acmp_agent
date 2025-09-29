
import math

def main():
    with open('INPUT.TXT', 'r') as f:
        n = int(f.readline().strip())
        directions = []
        for _ in range(n):
            data = f.readline().split()
            direction = int(data[0])
            steps = int(data[1])
            directions.append((direction, steps))
    
    x, y = 0.0, 0.0
    
    for direction, steps in directions:
        if direction == 1:  # север
            y += steps
        elif direction == 2:  # северо-восток
            x += steps * math.sqrt(2)/2
            y += steps * math.sqrt(2)/2
        elif direction == 3:  # восток
            x += steps
        elif direction == 4:  # юго-восток
            x += steps * math.sqrt(2)/2
            y -= steps * math.sqrt(2)/2
        elif direction == 5:  # юг
            y -= steps
        elif direction == 6:  # юго-запад
            x -= steps * math.sqrt(2)/2
            y -= steps * math.sqrt(2)/2
        elif direction == 7:  # запад
            x -= steps
        elif direction == 8:  # северо-запад
            x -= steps * math.sqrt(2)/2
            y += steps * math.sqrt(2)/2
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(f"{x:.3f} {y:.3f}")

if __name__ == "__main__":
    main()
