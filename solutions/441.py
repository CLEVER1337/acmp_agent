
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    a = list(map(int, data[1:1+n]))
    b = list(map(int, data[1+n:1+2*n]))
    
    if sorted(a) != sorted(b):
        print(-1)
        return
        
    pos_in_b = {}
    for idx, num in enumerate(b):
        pos_in_b[num] = idx
        
    target_indices = [pos_in_b[num] for num in a]
    
    swaps = 0
    for i in range(n):
        for j in range(n - i - 1):
            if target_indices[j] > target_indices[j + 1]:
                target_indices[j], target_indices[j + 1] = target_indices[j + 1], target_indices[j]
                swaps += 1
                
    print(swaps)

if __name__ == "__main__":
    main()
