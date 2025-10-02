
import math

def main():
    data = input().split()
    R = float(data[0])
    L = int(data[1])
    
    count = 0
    max_grid = math.floor(R / L)
    
    for x in range(-max_grid, max_grid + 1):
        for y in range(-max_grid, max_grid + 1):
            x_left = x * L
            y_bottom = y * L
            x_right = (x + 1) * L
            y_top = (y + 1) * L
            
            farthest_x = max(abs(x_left), abs(x_right))
            farthest_y = max(abs(y_bottom), abs(y_top))
            
            if math.sqrt(farthest_x**2 + farthest_y**2) <= R:
                count += 1
                
    print(count)

if __name__ == "__main__":
    main()
