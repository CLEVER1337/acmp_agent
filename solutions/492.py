
def main():
    import math
    
    with open("INPUT.TXT", "r") as f:
        x0, y0 = map(int, f.readline().split())
        Vx, Vy = map(int, f.readline().split())
        V, t, d = map(int, f.readline().split())
    
    xt = x0 + Vx * t
    yt = y0 + Vy * t
    
    max_distance = V * t
    
    if abs(d - math.sqrt(xt**2 + yt**2)) <= max_distance:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
