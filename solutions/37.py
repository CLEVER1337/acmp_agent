
import math

def main():
    data = input().split()
    n = int(data[0])
    q = float(data[1])
    
    is_compressing = True
    
    for _ in range(n):
        coords = list(map(int, input().split()))
        x1, y1, x2, y2 = coords
        
        norm_x = math.sqrt(x1*x1 + y1*y1)
        norm_ax = math.sqrt(x2*x2 + y2*y2)
        
        if norm_x == 0:
            if norm_ax > 0:
                is_compressing = False
                break
            continue
            
        if norm_ax > q * norm_x + 1e-9:
            is_compressing = False
            break
            
    print("Yes" if is_compressing else "No")

if __name__ == "__main__":
    main()
