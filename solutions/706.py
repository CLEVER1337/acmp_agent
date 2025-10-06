
import math

def main():
    data = input().split()
    R = int(data[0])
    X = int(data[1])
    Y = int(data[2])
    
    if X == 0 and Y == 0:
        print("{:.2f}".format(R))
        return
        
    angle = math.atan2(Y, X)
    target_angle = 2 * angle - math.pi / 2
    
    result = R * math.tan(target_angle)
    print("{:.2f}".format(result))

if __name__ == "__main__":
    main()
