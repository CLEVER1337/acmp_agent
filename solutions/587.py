
import sys
from math import sin, cos, radians

def read_input():
    n = int(sys.stdin.readline())
    engines = []
    for i in range(n):
        thrust, angle = map(float, sys.stdin.readline().split())
        engines.append((thrust * sin(radians(angle)), thrust * cos(radians(angle))))
    return engines

def solve():
    engines = read_input()
    engines.sort(reverse=True)
    
    total_x, total_y = 0, 0
    result = []
    for i in range(len(engines)):
        if not result or (total_x * total_y >= total_x * engines[i][1] + total_y * engines[i][0]):
            total_x += engines[i][0]
            total_y += engines[i][1]
            result.append(i + 1)
    
    print(len(result))
    print(' '.join(map(str, result)))

if __name__ == '__main__':
    solve()
