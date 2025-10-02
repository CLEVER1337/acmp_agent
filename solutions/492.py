
import math

def main():
    with open('INPUT.TXT', 'r') as f:
        x0, y0 = map(int, f.readline().split())
        Vx, Vy = map(int, f.readline().split())
        V, t, d = map(int, f.readline().split())
    
    xt = x0 + Vx * t
    yt = y0 + Vy * t
    
    max_distance = V * t
    
    if abs(d - math.sqrt(xt*xt + yt*yt)) <= max_distance + 1e-9:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
