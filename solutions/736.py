
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    k = int(data[1])
    l = int(data[2])
    queries = list(map(int, data[3:3+l]))
    
    if k == 1:
        for q in queries:
            if q <= n:
                print(q)
            else:
                print(0)
        return
        
    res = []
    for q in queries:
        if q > n:
            res.append(0)
            continue
            
        pos = q
        time = 0
        step = 1
        total_removed = 0
        current_n = n
        
        while True:
            if k > current_n:
                break
                
            full_cycles = (current_n) // k
            removed_in_step = full_cycles
            total_removed += removed_in_step
            
            if pos > current_n:
                break
                
            if k == 1:
                time += pos
                break
                
            cycle_num = (pos - 1) // k
            pos_in_cycle = (pos - 1) % k + 1
            
            if pos_in_cycle == 0:
                time += cycle_num + 1
                break
                
            if cycle_num < full_cycles:
                time += cycle_num + 1
                break
                
            pos = pos - full_cycles
            current_n -= full_cycles
            
        if time == 0:
            res.append(0)
        else:
            res.append(time)
            
    for ans in res:
        print(ans)

if __name__ == "__main__":
    main()
