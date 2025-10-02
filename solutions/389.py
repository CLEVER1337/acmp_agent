
import sys

def is_gray(arr, n):
    size = len(arr)
    for i in range(size):
        prev = arr[(i - 1) % size]
        curr = arr[i]
        next_val = arr[(i + 1) % size]
        
        diff_prev = bin(prev ^ curr).count('1')
        diff_next = bin(curr ^ next_val).count('1')
        
        if diff_prev != 1 or diff_next != 1:
            return False
    return True

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    arr = list(map(int, data[1:1+2**n]))
    m = int(data[1+2**n])
    
    results = []
    idx = 1 + 2**n + 1
    
    for _ in range(m):
        i = int(data[idx])
        j = int(data[idx+1])
        idx += 2
        
        arr[i], arr[j] = arr[j], arr[i]
        
        if is_gray(arr, n):
            results.append("Yes")
        else:
            results.append("No")
    
    for res in results:
        print(res)

if __name__ == "__main__":
    main()
