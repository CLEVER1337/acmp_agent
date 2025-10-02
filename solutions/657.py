
import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    
    k = int(data[0])
    index = 1
    results = []
    
    for _ in range(k):
        n = int(data[index]); index += 1
        T = list(map(int, data[index:index+n]))
        index += n
        
        if n < 3:
            results.append("ERROR")
            continue
            
        total_time = sum(T)
        segments = n
        expected_T = total_time / segments
        
        bits = []
        valid = True
        
        for i in range(n):
            if i % 2 == 0:
                if T[i] < expected_T * 0.9 or T[i] > expected_T * 1.1:
                    valid = False
                    break
            else:
                if T[i] < expected_T * 0.9 or T[i] > expected_T * 1.1:
                    valid = False
                    break
        
        if not valid:
            results.append("ERROR")
            continue
            
        bits = []
        for i in range(0, n-2, 2):
            if T[i] + T[i+2] > T[i+1] * 1.1:
                bits.append('1')
            else:
                bits.append('0')
        
        if len(bits) == 0:
            results.append("ERROR")
        else:
            results.append('1' + ''.join(bits) + '0')
    
    for res in results:
        print(res)

if __name__ == "__main__":
    solve()
