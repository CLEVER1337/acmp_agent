
import math

def main():
    with open("INPUT.TXT", "r") as f:
        data = f.readline().split()
        R = float(data[0])
        L = int(data[1])
    
    cells = 0
    half_L = L / 2.0
    
    max_grid = int(math.floor(R / L)) + 1
    
    for i in range(max_grid):
        x = i * L + half_L
        if x > R:
            continue
            
        for j in range(max_grid):
            y = j * L + half_L
            if y > R:
                continue
                
            distance = math.sqrt(x*x + y*y)
            if distance <= R:
                cells += 1
                
    cells = cells * 4 - 4 * max_grid + 1
    
    print(cells)

if __name__ == "__main__":
    main()
