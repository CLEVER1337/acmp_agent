
import math

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    k_list = list(map(int, data[1:1+n]))
    
    results = []
    for k in k_list:
        if k == 0:
            results.append("1 2")
            continue
            
        a = int((1 + math.sqrt(1 + 8 * k)) / 2)
        while a * (a - 1) // 2 <= k:
            a += 1
        a -= 1
        
        rem = k - a * (a - 1) // 2
        b = a + rem + 1
        results.append(f"{a} {b}")
    
    for res in results:
        print(res)

if __name__ == "__main__":
    main()
