
import math

def main():
    with open("INPUT.TXT", "r") as f:
        x1, y1, x2, y2 = map(int, f.read().split())
    
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    
    gcd = math.gcd(dx, dy)
    result = gcd + 1
    
    with open("OUTPUT.TXT", "w") as f:
        f.write(str(result))

if __name__ == "__main__":
    main()
