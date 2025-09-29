
import math

def check_circles(circle1, circle2):
    x1, y1, r1 = circle1
    x2, y2, r2 = circle2
    
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    if distance > r1 + r2:
        return "NO"
    else:
        return "YES"

with open('INPUT.TXT', 'r') as file:
    circle1 = list(map(int, file.readline().split()))
    circle2 = list(map(int, file.readline().split()))
    
result = check_circles(circle1, circle2)

with open('OUTPUT.TXT', 'w') as file:
    file.write(result)
