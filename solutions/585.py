
import math

def main():
    with open('INPUT.TXT', 'r') as f:
        N = f.readline().strip()
        if not N:
            print(-1)
            return
            
        n = int(N)
        log10_2 = math.log10(2)
        log10_n = math.log10(n)
        log10_n1 = math.log10(n + 1)
        
        k = 1
        while True:
            log10_2k = k * log10_2
            fractional = log10_2k - math.floor(log10_2k)
            lower_bound = 10 ** fractional
            
            if lower_bound >= n and lower_bound < n + 1:
                break
                
            k += 1
            if k > 10**7:
                k = -1
                break
                
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(k))

if __name__ == '__main__':
    main()
