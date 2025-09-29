
import math

def main():
    with open('INPUT.TXT', 'r') as f:
        data = f.readline().split()
        x1, y1, x2, y2 = map(int, data)
    
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write("{:.5f}".format(distance))

if __name__ == "__main__":
    main()
