
import math

def main():
    with open('INPUT.TXT', 'r') as f:
        n = int(f.readline().strip())
        points = []
        for _ in range(n):
            x, y = map(int, f.readline().split())
            points.append((x, y))
    
    total_distance = 0.0
    current_x, current_y = 0, 0
    
    for point in points:
        x, y = point
        distance = math.sqrt((x - current_x)**2 + (y - current_y)**2)
        total_distance += distance
        current_x, current_y = x, y
    
    distance_home = math.sqrt(current_x**2 + current_y**2)
    total_distance += distance_home
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write("{:.3f}".format(total_distance))

if __name__ == "__main__":
    main()
