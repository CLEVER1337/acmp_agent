
import sys

def main():
    data = sys.stdin.read().split()
    index = 0
    k = int(data[index]); index += 1
    results = []
    
    for _ in range(k):
        n = int(data[index]); index += 1
        guards = []
        for i in range(n):
            a = int(data[index]); b = int(data[index+1]); index += 2
            guards.append((a, b))
        
        max_time = 10000
        timeline = [0] * (max_time + 2)
        
        for a, b in guards:
            timeline[a] += 1
            timeline[b] -= 1
        
        current = 0
        for i in range(max_time + 1):
            current += timeline[i]
            timeline[i] = current
        
        critical_guards = 0
        valid = True
        
        for i in range(max_time):
            if timeline[i] == 0:
                valid = False
                break
        
        if not valid:
            results.append("Wrong Answer")
            continue
        
        for i in range(n):
            a, b = guards[i]
            temp_timeline = timeline.copy()
            
            for t in range(a, b):
                temp_timeline[t] -= 1
            
            uncovered = False
            for t in range(max_time):
                if temp_timeline[t] == 0:
                    uncovered = True
                    break
            
            if not uncovered:
                critical_guards += 1
        
        if critical_guards == n:
            results.append("Accepted")
        else:
            results.append("Wrong Answer")
    
    for res in results:
        print(res)

if __name__ == "__main__":
    main()
