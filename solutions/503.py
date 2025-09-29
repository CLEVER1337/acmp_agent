
import sys
from itertools import permutations

def main():
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    planets = []
    for i in range(1, n+1):
        parts = data[i].split()
        p_type = parts[0]
        c_to = int(parts[1])
        p_to = int(parts[2])
        c_from = int(parts[3])
        p_from = int(parts[4])
        planets.append((p_type, c_to, p_to, c_from, p_from))
    
    min_cak = float('inf')
    best_route = None
    
    for perm in permutations(range(n)):
        total_cak = 0
        current_chatlans = 0
        current_patsaks = 0
        
        for planet_idx in perm:
            p_type, c_to, p_to, c_from, p_from = planets[planet_idx]
            
            if p_type == 'C':
                total_cak += current_patsaks * c_to
            else:
                total_cak += current_chatlans * p_to
            
            current_chatlans += c_to
            current_patsaks += p_to
            
            if p_type == 'C':
                total_cak += current_patsaks * c_from
            else:
                total_cak += current_chatlans * p_from
            
            current_chatlans -= c_from
            current_patsaks -= p_from
        
        if total_cak < min_cak:
            min_cak = total_cak
            best_route = perm
        elif total_cak == min_cak:
            if best_route is None or perm < best_route:
                best_route = perm
    
    result_route = [0] + [x+1 for x in best_route] + [0]
    print(min_cak)
    print(" ".join(map(str, result_route)))

if __name__ == "__main__":
    main()
