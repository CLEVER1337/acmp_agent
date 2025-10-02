
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        print(0)
        return
        
    n = int(data[0])
    m = int(data[1])
    k = int(data[2])
    
    bad_cells = []
    index = 3
    for i in range(k):
        r = int(data[index])
        c = int(data[index + 1])
        index += 2
        bad_cells.append((r, c))
    
    total_rectangles = n * (n + 1) // 2 * m * (m + 1) // 2
    
    if k == 0:
        print(total_rectangles)
        return
        
    bad_cells.sort(key=lambda x: (x[0], x[1]))
    
    left_bound = [0] * (n + 2)
    right_bound = [m + 1] * (n + 2)
    
    for r, c in bad_cells:
        left_bound[r] = max(left_bound[r], c)
        right_bound[r] = min(right_bound[r], c)
    
    result = 0
    
    for top in range(1, n + 1):
        L = [0] * (m + 2)
        R = [m + 1] * (m + 2)
        
        for bottom in range(top, n + 1):
            L[bottom] = max(L[bottom - 1], left_bound[bottom])
            R[bottom] = min(R[bottom - 1], right_bound[bottom])
            
            if L[bottom] >= R[bottom]:
                continue
                
            result += (R[bottom] - L[bottom] - 1)
    
    print(total_rectangles - result)

if __name__ == "__main__":
    main()
