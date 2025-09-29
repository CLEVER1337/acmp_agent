
import math

def main():
    with open('INPUT.TXT', 'r') as f:
        n_str = f.readline().strip()
        if not n_str:
            print(-1)
            return
            
        n = int(n_str)
        if n <= 0:
            print(-1)
            return
            
        log10_2 = math.log10(2)
        log10_n = math.log10(n)
        log10_n_plus_1 = math.log10(n + 1)
        
        k = 1
        found = False
        
        while True:
            log10_2k = k * log10_2
            fractional = log10_2k - math.floor(log10_2k)
            
            start_num = 10 ** fractional
            
            if n <= start_num < n + 1:
                found = True
                break
                
            k += 1
            
            if k > 10000000:
                break
                
        if found:
            print(k)
        else:
            print(-1)

if __name__ == "__main__":
    main()
