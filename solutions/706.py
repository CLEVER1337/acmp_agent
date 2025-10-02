
import math

def main():
    with open('INPUT.TXT', 'r') as f:
        R, X, Y = map(int, f.read().split())
    
    if X == 0:
        result = 0.0
    else:
        sign = 1 if X > 0 else -1
        result = sign * R * (R - Y) / (2 * R - Y)
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write("{:.2f}".format(result))

if __name__ == "__main__":
    main()
