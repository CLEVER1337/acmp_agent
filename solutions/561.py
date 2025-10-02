
import sys
import math

def log_tower_value(tower):
    if len(tower) == 1:
        return math.log(tower[0])
    
    result = math.log(tower[-1])
    for i in range(len(tower)-2, -1, -1):
        result = result * tower[i]
    
    return result

def main():
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    towers = []
    
    for i in range(1, n+1):
        parts = list(map(int, data[i].split()))
        k = parts[0]
        tower = parts[1:1+k]
        towers.append((i-1, tower))
    
    def compare_towers(tower1, tower2):
        idx1, t1 = tower1
        idx2, t2 = tower2
        
        if len(t1) == 1 and len(t2) == 1:
            return t1[0] - t2[0]
        
        if t1[0] == 1 and t2[0] == 1:
            return 0
        
        if t1[0] == 1:
            return -1
        
        if t2[0] == 1:
            return 1
        
        log_val1 = log_tower_value(t1)
        log_val2 = log_tower_value(t2)
        
        if abs(log_val1 - log_val2) < 1e-10:
            return 0
        elif log_val1 < log_val2:
            return -1
        else:
            return 1
    
    sorted_towers = sorted(towers, key=lambda x: (x[1], x[0]))
    
    result = [str(idx + 1) for idx, _ in sorted_towers]
    print(" ".join(result))

if __name__ == "__main__":
    main()
