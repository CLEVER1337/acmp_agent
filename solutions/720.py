
import math

def main():
    data = input().split()
    R = float(data[0])
    L = int(data[1])
    
    count = 0
    half_L = L / 2.0
    
    max_grid = int(math.floor(R / L)) + 1
    
    for i in range(max_grid):
        x = i * L + half_L
        if x > R:
            continue
            
        max_j = int(math.floor(math.sqrt(R*R - x*x) / L))
        count += max_j + 1
        
    total = 4 * count
    
    print(total)

if __name__ == "__main__":
    main()
