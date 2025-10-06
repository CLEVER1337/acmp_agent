
import math

def main():
    data = []
    for _ in range(3):
        line = input().split()
        data.append(list(map(int, line)))
    
    x0, y0 = data[0]
    Vx, Vy = data[1]
    V, t, d = data[2]
    
    tx = x0 + Vx * t
    ty = y0 + Vy * t
    
    max_distance = V * t
    
    if d > max_distance + math.sqrt(tx*tx + ty*ty):
        print("NO")
        return
        
    if d < abs(math.sqrt(tx*tx + ty*ty) - max_distance):
        print("NO")
        return
        
    a = Vx*Vx + Vy*Vy - V*V
    b = 2*(x0*Vx + y0*Vy)
    c = x0*x0 + y0*y0 - d*d
    
    discriminant = b*b - 4*a*c
    
    if a == 0:
        if b != 0:
            T = -c / b
            if 0 <= T <= t:
                print("YES")
            else:
                print("NO")
        else:
            if c == 0:
                print("YES")
            else:
                print("NO")
        return
        
    if discriminant < 0:
        print("NO")
        return
        
    sqrt_discr = math.sqrt(discriminant)
    T1 = (-b - sqrt_discr) / (2 * a)
    T2 = (-b + sqrt_discr) / (2 * a)
    
    if (0 <= T1 <= t) or (0 <= T2 <= t) or (T1 <= t <= T2) or (T2 <= t <= T1):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
