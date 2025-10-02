
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        print(0)
        return
        
    n = int(data[0])
    k = int(data[1])
    a = list(map(int, data[2:2+n]))
    
    count = [0] * (n + 2)
    max_prefix = n
    
    for j in range(n):
        num = a[j]
        count[num] += 1
        
        if num > 0:
            prev_count = count[num - 1]
            if prev_count < count[num] - k:
                max_prefix = j
                break
                
    print(max_prefix)

if __name__ == "__main__":
    main()
