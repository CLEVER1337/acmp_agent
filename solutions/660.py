
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
    
    if k == 0:
        total = n * (n + 1) // 2 * m * (m + 1) // 2
        print(total)
        return
        
    bad_cells.sort()
    
    left_bound = [0] * (n + 2)
    right_bound = [m + 1] * (n + 2)
    
    for r, c in bad_cells:
        if left_bound[r] == 0:
            left_bound[r] = c
            right_bound[r] = c
        else:
            left_bound[r] = min(left_bound[r], c)
            right_bound[r] = max(right_bound[r], c)
    
    total = 0
    
    for top in range(1, n + 1):
        L = [0] * (m + 2)
        R = [m + 1] * (m + 2)
        
        for bottom in range(top, n + 1):
            if left_bound[bottom] != 0:
                L[left_bound[bottom]] = max(L[left_bound[bottom]], right_bound[bottom])
                R[right_bound[bottom]] = min(R[right_bound[bottom]], left_bound[bottom])
            
            left_most = 0
            count = 0
            
            for right in range(1, m + 1):
                left_most = max(left_most, L[right])
                if left_most < right:
                    count += (right - left_most)
            
            total += count
            
            left_most = m + 1
            for left in range(m, 0, -1):
                left_most = min(left_most, R[left])
                if left_most > left:
                    total -= (left_most - left)
    
    print(total)

if __name__ == "__main__":
    main()
