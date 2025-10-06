
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    k = int(data[0])
    index = 1
    results = []
    
    for _ in range(k):
        n = int(data[index]); index += 1
        T_list = list(map(int, data[index:index+n]))
        index += n
        
        total_time = sum(T_list)
        T_val = total_time / ((n + 1) // 2)
        
        signal = ['1']
        for i in range(1, n-1, 2):
            t1 = T_list[i]
            t2 = T_list[i+1]
            
            expected_half = T_val / 2
            lower_bound1 = expected_half * 0.9
            upper_bound1 = expected_half * 1.1
            
            if lower_bound1 <= t1 <= upper_bound1:
                signal.append('0')
            else:
                signal.append('1')
                
            if i + 2 < n:
                signal.append('1')
        
        signal.append('0')
        
        if len(signal) != (n + 1) // 2:
            results.append("ERROR")
        else:
            results.append(''.join(signal))
    
    for res in results:
        print(res)

if __name__ == "__main__":
    main()
