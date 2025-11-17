
from sympy import *

def tower_value(tower):
    k = tower[0]
    tower = tower[1:]
    value = 0
    for i in range(len(tower)):
        value += tower[-i-1]*X**i if i <= k else 0
    return value

def solve_problem():
    with open('INPUT.TXT', 'r') as input_file, open('OUTPUT.TXT', 'w') as output_file:
        N = int(input_file.readline())
        towers = []
        for i in range(N):
            tower = list(map(int, input_file.readline().split()))
            towers.append((tower_value(tower), i+1))
        towers.sort()
        output_file.write(' '.join([str(i) for _, i in towers]))

if __name__ == '__main__':
    solve_problem()
