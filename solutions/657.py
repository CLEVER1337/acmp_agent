
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
        T = list(map(int, data[index:index+n]))
        index += n
        
        if n < 3:
            results.append("ERROR")
            continue
            
        segments = []
        for i in range(n):
            segments.append(T[i])
            
        total_time = sum(segments)
        expected_T = total_time / ((n + 1) / 2)
        
        bits = []
        valid = True
        
        current_pos = 0
        for i in range((n - 1) // 2):
            first_half = segments[2*i]
            second_half = segments[2*i + 1]
            next_first = segments[2*i + 2]
            
            ratio1 = first_half / (first_half + second_half)
            ratio2 = second_half / (first_half + second_half)
            
            if abs(ratio1 - 0.5) / 0.5 <= 0.1 and abs(ratio2 - 0.5) / 0.5 <= 0.1:
                bits.append('1')
            elif abs(ratio1 - 0.5) / 0.5 <= 0.1 and abs(ratio2 - 0.5) / 0.5 <= 0.1:
                bits.append('0')
            else:
                if ratio1 > ratio2:
                    bits.append('1')
                else:
                    bits.append('0')
                    
        if len(bits) != (n - 1) // 2:
            results.append("ERROR")
            continue
            
        if bits[0] != '1' or bits[-1] != '0':
            if bits[0] != '1':
                bits[0] = '1'
            if bits[-1] != '0':
                bits[-1] = '0'
                
        results.append(''.join(bits))
        
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
