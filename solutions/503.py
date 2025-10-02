
import sys
from itertools import permutations

def main():
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    planets = []
    for i in range(1, n+1):
        parts = data[i].split()
        p_type = parts[0]
        to_planet_chatl = int(parts[1])
        to_planet_pac = int(parts[2])
        from_planet_chatl = int(parts[3])
        from_planet_pac = int(parts[4])
        planets.append((p_type, to_planet_chatl, to_planet_pac, from_planet_chatl, from_planet_pac))
    
    min_cost = float('inf')
    best_order = []
    
    for perm in permutations(range(n)):
        cost = 0
        current_chatlans = 0
        current_pacs = 0
        
        for idx in perm:
            p_type, to_chatl, to_pac, from_chatl, from_pac = planets[idx]
            
            if p_type == 'P':
                cost += current_chatlans
            else:
                cost += current_pacs
            
            current_chatlans += to_chatl
            current_pacs += to_pac
        
        for idx in perm:
            p_type, to_chatl, to_pac, from_chatl, from_pac = planets[idx]
            
            current_chatlans -= to_chatl
            current_pacs -= to_pac
            
            if p_type == 'P':
                cost += current_chatlans
            else:
                cost += current_pacs
            
            current_chatlans += from_chatl
            current_pacs += from_pac
        
        if cost < min_cost:
            min_cost = cost
            best_order = list(perm)
        elif cost == min_cost:
            if tuple(best_order) > tuple(perm):
                best_order = list(perm)
    
    best_order = [x+1 for x in best_order]
    print(min_cost)
    print("0", " ".join(map(str, best_order)), "0")

if __name__ == "__main__":
    main()
