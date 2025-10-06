
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        print(0)
        return
        
    k = int(data[0])
    m = list(map(int, data[1:1+k]))
    
    total = sum(m)
    if total == 0:
        print(1)
        print(0)
        return
        
    n = len(m)
    res = []
    
    for i in range(n):
        if i == n - 1 or m[i] > m[i+1]:
            if m[i] > 1:
                new_m = m.copy()
                new_m[i] -= 1
                if i == n - 1 or new_m[i] >= new_m[i+1]:
                    res.append(new_m)
                else:
                    j = i + 1
                    while j < n and new_m[i] < new_m[j]:
                        j += 1
                    temp = new_m[i]
                    new_m = new_m[:i+1] + [temp] + new_m[i+1:j] + new_m[j+1:]
                    res.append(new_m)
            else:
                new_m = m[:i] + m[i+1:]
                res.append(new_m)
                
        if i < n - 1 and m[i] == m[i+1]:
            if i == 0 or m[i-1] > m[i]:
                new_m = m.copy()
                new_m[i] -= 1
                new_m[i+1] -= 1
                if new_m[i] == 0:
                    new_m = new_m[:i] + new_m[i+2:]
                elif new_m[i+1] == 0:
                    new_m = new_m[:i+1] + new_m[i+2:]
                res.append(new_m)
                
    unique_res = []
    seen = set()
    for diagram in res:
        key = tuple(diagram)
        if key not in seen:
            seen.add(key)
            unique_res.append(diagram)
            
    unique_res.sort(key=lambda x: (-len(x), x))
    
    print(len(unique_res))
    for diagram in unique_res:
        print(len(diagram), end=' ')
        print(' '.join(map(str, diagram)))
        
if __name__ == "__main__":
    main()
