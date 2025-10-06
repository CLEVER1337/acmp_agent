
import math

def main():
    tw, th, w, h = map(int, input().split())
    
    def check(a, b, c, d):
        if a % c == 0 and b % d == 0:
            return True
        if a % d == 0 and b % c == 0:
            return True
            
        if c > a or d > b:
            return False
            
        rem1 = a % c
        rem2 = b % d
        if rem1 == 0:
            if b >= d:
                return True
        if rem2 == 0:
            if a >= c:
                return True
                
        if a >= c and b >= d:
            if (a % c) % d == 0 and (b % d) % c == 0:
                return True
            if (a % d) % c == 0 and (b % c) % d == 0:
                return True
                
        return False
        
    if check(w, h, tw, th) or check(w, h, th, tw):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
