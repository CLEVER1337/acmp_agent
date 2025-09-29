
import sys

def is_gray_sequence(arr, n):
    total = len(arr)
    for i in range(total):
        current = arr[i]
        left = arr[(i - 1) % total]
        right = arr[(i + 1) % total]
        
        diff_left = current ^ left
        diff_right = current ^ right
        
        if bin(diff_left).count('1') != 1 or bin(diff_right).count('1') != 1:
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
    current_arr = arr.copy()
    
    index = 1 + 2**n + 1
    for _ in range(m):
        i = int(data[index])
        j = int(data[index+1])
        index += 2
        
        current_arr[i], current_arr[j] = current_arr[j], current_arr[i]
        
        if is_gray_sequence(current_arr, n):
            results.append("Yes")
        else:
            results.append("No")
    
    for res in results:
        print(res)

if __name__ == "__main__":
    main()
