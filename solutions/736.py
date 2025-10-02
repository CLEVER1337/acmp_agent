
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
        for query in queries:
            if query <= n:
                print(query)
            else:
                print(0)
        return
    
    answers = []
    for pos in queries:
        if pos > n:
            answers.append(0)
            continue
            
        time = 0
        current_pos = pos
        step = 1
        total_removed = 0
        
        while True:
            if current_pos % k != 0:
                break
                
            round_num = current_pos // k
            if round_num == 0:
                break
                
            time += round_num
            current_pos = round_num
            
        answers.append(time)
    
    for ans in answers:
        print(ans)

if __name__ == "__main__":
    main()
