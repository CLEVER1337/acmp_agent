
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
        covered = True
        for i in range(max_time):
            current += timeline[i]
            if current <= 0:
                covered = False
                break
        
        if not covered:
            results.append("Wrong Answer")
            continue
        
        essential_count = 0
        valid = True
        
        for i in range(n):
            a, b = guards[i]
            timeline2 = timeline.copy()
            timeline2[a] -= 1
            timeline2[b] += 1
            
            current = 0
            uncovered = False
            for t in range(max_time):
                current += timeline2[t]
                if current <= 0:
                    uncovered = True
                    break
            
            if not uncovered:
                valid = False
                break
            else:
                essential_count += 1
        
        if valid and essential_count == n:
            results.append("Accepted")
        else:
            results.append("Wrong Answer")
    
    for res in results:
        print(res)

if __name__ == "__main__":
    main()
