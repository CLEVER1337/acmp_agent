
import sys

def main():
    data = sys.stdin.read().split()
    k = int(data[0])
    index = 1
    results = []
    
    for _ in range(k):
        a = int(data[index]); b = int(data[index+1]); index += 2
        c = int(data[index]); d = int(data[index+1]); index += 2
        
        if c == 0 or d == 0:
            results.append("NO")
            continue
            
        if a == c and b == d:
            results.append("YES")
            continue
            
        if c > a or d > b:
            results.append("NO")
            continue
            
        found = False
        while a > 0 and b > 0:
            if a == c and b == d:
                found = True
                break
            if a > b:
                if b == 0:
                    break
                if d == b and c <= a and (a - c) % b == 0:
                    found = True
                    break
                a %= b
            else:
                if a == 0:
                    break
                if c == a and d <= b and (b - d) % a == 0:
                    found = True
                    break
                b %= a
                
        results.append("YES" if found else "NO")
    
    for res in results:
        print(res)

if __name__ == "__main__":
    main()
