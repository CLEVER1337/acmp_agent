
import math

def calculate_surface(d, r, l):
    return 2 * math.pi * r * (r + l) - d**2 * math.pi / 4

if __name__ == '__main__':
    with open('INPUT.TXT', 'r') as file:
        r, l, d = map(int, file.read().split())
    
    left = 0
    right = 1e6
    while right - left > 1e-7:
        mid = (left + right) / 2
        if calculate_surface(mid, r, l) >= 2 * math.pi * r * (r + l):
            right = mid
        else:
            left = mid
    
    with open('OUTPUT.TXT', 'w') as file:
        file.write("{:.6f}".format(right))
