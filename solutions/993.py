
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    k = int(data[1])
    a = list(map(int, data[2:2+n]))
    
    freq = [0] * (n + 1)
    min_count = [0] * (n + 1)
    max_count = [0] * (n + 1)
    
    p = 0
    for j in range(n):
        num = a[j]
        freq[num] += 1
        if freq[num] > max_count[num]:
            max_count[num] = freq[num]
        
        for i in range(num):
            if min_count[i] < max_count[num] - k:
                break
        else:
            p = j + 1
            continue
            
        for i in range(num + 1, n + 1):
            if min_count[i] < max_count[num] - k:
                break
        else:
            p = j + 1
            continue
            
        break
        
    print(p)

if __name__ == "__main__":
    main()
