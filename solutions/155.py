
import sys
from itertools import permutations

def parse_input():
    data = sys.stdin.read().splitlines()
    if not data:
        return None, None, None
    
    n_c_line = data[0].split()
    n = int(n_c_line[0])
    c = float(n_c_line[1])
    
    capacitors = list(map(float, data[1].split()))
    return n, c, capacitors

def series(c1, c2):
    return (c1 * c2) / (c1 + c2) if c1 + c2 != 0 else 0

def parallel(c1, c2):
    return c1 + c2

def generate_circuits(capacitors):
    if len(capacitors) == 1:
        return {capacitors[0]}
    
    results = set()
    n = len(capacitors)
    
    for i in range(1, n):
        for left_combo in permutations(capacitors, i):
            right_combo = tuple(x for x in capacitors if x not in left_combo)
            
            left_circuits = generate_circuits(left_combo)
            right_circuits = generate_circuits(right_combo)
            
            for left_cap in left_circuits:
                for right_cap in right_circuits:
                    results.add(series(left_cap, right_cap))
                    results.add(parallel(left_cap, right_cap))
    
    return results

def solve():
    n, target_c, capacitors = parse_input()
    if n is None:
        return "NO"
    
    all_possible = set()
    
    for i in range(1, n + 1):
        for combo in permutations(capacitors, i):
            circuits = generate_circuits(combo)
            all_possible.update(circuits)
    
    for capacitance in all_possible:
        if abs(capacitance - target_c) <= 0.01:
            return "YES"
    
    return "NO"

if __name__ == "__main__":
    result = solve()
    print(result)
