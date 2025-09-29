
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    k = int(data[1])
    a = list(map(int, data[2:2+n]))
    
    cnt = [0] * (n + 2)
    min_count = [0] * (n + 2)
    max_count = [0] * (n + 2)
    
    p = 0
    for j in range(n):
        num = a[j]
        cnt[num] += 1
        if cnt[num] > max_count[num]:
            max_count[num] = cnt[num]
        
        if num > 0:
            min_count[num] = min(min_count[num], cnt[num])
        else:
            min_count[num] = cnt[num]
            
        valid = True
        for i in range(num):
            if cnt[i] < max_count[num] - k:
                valid = False
                break
                
        if not valid:
            break
            
        p = j + 1
        
    print(p)

if __name__ == "__main__":
    main()
