
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    size = 1 << n
    arr = list(map(int, data[1:1+size]))
    m = int(data[1+size])
    swaps = []
    index = 2 + size
    for i in range(m):
        i1 = int(data[index]); i2 = int(data[index+1])
        swaps.append((i1, i2))
        index += 2
        
    def is_gray_neighbors(a, b):
        xor_val = a ^ b
        return xor_val & (xor_val - 1) == 0 and xor_val != 0
        
    def check_gray(arr):
        for i in range(size):
            left = arr[i-1]
            right = arr[(i+1) % size]
            current = arr[i]
            if not (is_gray_neighbors(current, left) and is_gray_neighbors(current, right)):
                return False
        return True
        
    results = []
    for i1, i2 in swaps:
        arr[i1], arr[i2] = arr[i2], arr[i1]
        if check_gray(arr):
            results.append("Yes")
        else:
            results.append("No")
            
    for res in results:
        print(res)

if __name__ == "__main__":
    main()
