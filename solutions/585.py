
import math

def main():
    with open('INPUT.TXT', 'r') as f:
        n_str = f.readline().strip()
        if not n_str:
            print(-1)
            return
        
        n = int(n_str)
        
        if n == 0:
            print(-1)
            return
            
        log2_10 = math.log(10, 2)
        log2_n = math.log(n, 2)
        log2_n1 = math.log(n + 1, 2)
        
        k = 1
        while True:
            fractional = k * log2_10 - math.floor(k * log2_10)
            lower_bound = 2 ** fractional
            upper_bound = 2 ** (fractional + log2_n1 - log2_n)
            
            if lower_bound >= n and lower_bound < n + 1:
                break
                
            if upper_bound >= n and upper_bound < n + 1:
                break
                
            k += 1
            
            if k > 10000000:
                print(-1)
                return
                
        with open('OUTPUT.TXT', 'w') as out:
            out.write(str(k))

if __name__ == "__main__":
    main()
