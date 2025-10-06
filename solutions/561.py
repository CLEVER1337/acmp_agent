
import sys
import math

def log_tower_value(tower):
    if len(tower) == 1:
        return math.log(tower[0])
    if tower[0] == 1:
        return 0.0
    
    result = math.log(tower[-1])
    for i in range(len(tower)-2, 0, -1):
        if result == 0:
            return 0.0
        result = math.log(tower[i]) * result
    result = math.log(tower[0]) * result
    return result

def main():
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    towers = []
    indices = []
    
    for idx, line in enumerate(data[1:1+n]):
        parts = list(map(int, line.split()))
        k = parts[0]
        tower = parts[1:1+k]
        towers.append((idx + 1, tower))
    
    def compare_key(item):
        idx, tower = item
        if len(tower) == 1:
            return (0, tower[0])
        
        if tower[0] == 1:
            return (0, 1)
        
        log_val = log_tower_value(tower)
        return (1, log_val)
    
    sorted_towers = sorted(towers, key=compare_key)
    result = [str(item[0]) for item in sorted_towers]
    print(" ".join(result))

if __name__ == "__main__":
    main()
