
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    k = int(data[1])
    l = int(data[2])
    queries = list(map(int, data[3:3+l]))
    
    if k == 1:
        for q in queries:
            if q <= n:
                print(q)
            else:
                print(0)
        return
    
    answers = []
    for q in queries:
        if q > n:
            answers.append(0)
            continue
            
        pos = q
        time = 0
        step = 1
        total_removed = 0
        
        while True:
            if pos % k != 0:
                pos -= pos // k
                time += step * (pos // k)
                step *= k
            else:
                break
                
            if pos < k:
                break
        
        if pos % k == 0:
            time += step * (pos // k)
        else:
            time = 0
            
        answers.append(time)
    
    for ans in answers:
        print(ans)

if __name__ == "__main__":
    main()
