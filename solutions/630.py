
import sys

def main():
    data = sys.stdin.read().split()
    index = 0
    k = int(data[index]); index += 1
    results = []
    
    for _ in range(k):
        n = int(data[index]); index += 1
        intervals = []
        for i in range(n):
            a = int(data[index]); b = int(data[index+1]); index += 2
            intervals.append((a, b))
        
        max_time = 10000
        covered = [0] * (max_time + 2)
        
        for a, b in intervals:
            covered[a] += 1
            if b + 1 <= max_time:
                covered[b + 1] -= 1
        
        for i in range(1, max_time + 1):
            covered[i] += covered[i - 1]
        
        fully_covered = True
        for i in range(max_time + 1):
            if covered[i] <= 0:
                fully_covered = False
                break
        
        if not fully_covered:
            results.append("Wrong Answer")
            continue
        
        critical_all = True
        for i in range(n):
            temp_covered = covered.copy()
            a, b = intervals[i]
            for t in range(a, b + 1):
                temp_covered[t] -= 1
            
            has_gap = False
            for t in range(max_time + 1):
                if temp_covered[t] <= 0:
                    has_gap = True
                    break
            
            if not has_gap:
                critical_all = False
                break
        
        if critical_all:
            results.append("Accepted")
        else:
            results.append("Wrong Answer")
    
    for res in results:
        print(res)

if __name__ == "__main__":
    main()
