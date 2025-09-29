
import sys
from itertools import permutations

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    k = int(data[1])
    
    a = []
    index = 2
    for i in range(n):
        row = list(map(int, data[index:index+n]))
        index += n
        a.append(row)
    
    t = list(map(int, data[index:index+n]))
    
    min_time = float('inf')
    best_path = []
    
    for subset_size in range(1, n + 1):
        for cities in permutations(range(1, n + 1), subset_size):
            if len(cities) != k:
                continue
                
            total_time = 0
            for i in range(len(cities)):
                city = cities[i]
                total_time += t[city - 1]
                
                if i > 0:
                    prev_city = cities[i - 1]
                    total_time += a[prev_city - 1][city - 1]
            
            if total_time < min_time:
                min_time = total_time
                best_path = list(cities)
    
    print(min_time)
    print(' '.join(map(str, best_path)))

if __name__ == "__main__":
    main()
