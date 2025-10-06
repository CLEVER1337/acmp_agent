
import sys

def main():
    data = sys.stdin.read().splitlines()
    index = 0
    output_lines = []
    while index < len(data):
        line = data[index].strip()
        if line == '':
            index += 1
            continue
        parts = line.split()
        n = int(parts[0])
        k = int(parts[1])
        if n == 0 and k == 0:
            break
            
        sets = []
        for i in range(k):
            index += 1
            s = data[index].strip().split()
            sets.append([int(x) for x in s])
        
        index += 1
        
        parent = list(range(n+1))
        set_id = [0] * (n+1)
        for i, s in enumerate(sets):
            for num in s:
                set_id[num] = i
        
        max_set = -1
        for i in range(k):
            if sets[i]:
                max_set = max(max_set, max(sets[i]))
        
        found = False
        new_sets = None
        
        for start in range(max_set, 0, -1):
            current_set_idx = set_id[start]
            if current_set_idx == -1:
                continue
                
            candidate = -1
            for num in range(start+1, n+1):
                if set_id[num] != current_set_idx:
                    if candidate == -1 or set_id[num] < set_id[candidate]:
                        candidate = num
            
            if candidate != -1:
                target_set_idx = set_id[candidate]
                sets[current_set_idx].remove(start)
                sets[target_set_idx].append(start)
                sets[target_set_idx].sort()
                set_id[start] = target_set_idx
                
                remaining = []
                for num in range(start+1, n+1):
                    if set_id[num] == current_set_idx:
                        remaining.append(num)
                
                if remaining:
                    new_set = []
                    for num in remaining:
                        set_id[num] = k
                        new_set.append(num)
                    sets[current_set_idx] = new_set
                    k += 1
                else:
                    sets.pop(current_set_idx)
                    k -= 1
                    for i in range(1, n+1):
                        if set_id[i] > current_set_idx:
                            set_id[i] -= 1
                
                for i in range(k):
                    sets[i].sort()
                
                sets.sort(key=lambda x: (len(x), x[0]) if x else (0, 0))
                sets.sort(key=lambda x: x[0] if x else 0)
                
                new_sets = sets
                found = True
                break
                
            else:
                sets[current_set_idx].remove(start)
                if not sets[current_set_idx]:
                    sets.pop(current_set_idx)
                    k -= 1
                    for i in range(1, n+1):
                        if set_id[i] > current_set_idx:
                            set_id[i] -= 1
                set_id[start] = -1
                new_set = [start]
                sets.append(new_set)
                k += 1
                set_id[start] = k-1
        
        if not found:
            new_sets = []
            for i in range(1, n+1):
                new_sets.append([i])
            k = n
        
        new_sets.sort()
        output_lines.append(f"{n} {k}")
        for s in new_sets:
            output_lines.append(" ".join(str(x) for x in s))
        output_lines.append("")
    
    sys.stdout.write("\n".join(output_lines))

if __name__ == "__main__":
    main()
