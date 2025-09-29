
import sys
import math

def log_tower_value(tower):
    if len(tower) == 1:
        return math.log(tower[0])
    
    value = math.log(tower[-1])
    for i in range(len(tower)-2, -1, -1):
        if value > 100:
            return float('inf')
        value = tower[i] * value
    
    return value

def compare_towers(tower1, tower2):
    if len(tower1) == 1 and len(tower2) == 1:
        return tower1[0] - tower2[0]
    
    if tower1[0] == 1 and tower2[0] == 1:
        return 0
    
    if tower1[0] == 1:
        return -1
    
    if tower2[0] == 1:
        return 1
    
    log1 = log_tower_value(tower1)
    log2 = log_tower_value(tower2)
    
    if abs(log1 - log2) < 1e-10:
        return 0
    return 1 if log1 > log2 else -1

def main():
    data = sys.stdin.read().splitlines()
    if not data:
        return
    
    n = int(data[0])
    towers = []
    
    for i in range(1, n + 1):
        parts = list(map(int, data[i].split()))
        k = parts[0]
        tower = parts[1:1 + k]
        towers.append((tower, i))
    
    def tower_key(item):
        tower, idx = item
        return (log_tower_value(tower), idx)
    
    sorted_towers = sorted(towers, key=tower_key)
    
    result = [str(idx) for _, idx in sorted_towers]
    print(" ".join(result))

if __name__ == "__main__":
    main()
