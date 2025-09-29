
import sys

def main():
    s = sys.stdin.readline().strip()
    if not s:
        print("NO")
        return
        
    n = len(s)
    i = 0
    
    while i < n:
        if not s[i].isupper():
            print("NO")
            return
            
        if i + 1 < n and s[i+1].islower():
            i += 2
        else:
            i += 1
            
        if i < n and s[i].isdigit():
            if i + 1 < n and s[i+1].isdigit():
                i += 2
            else:
                i += 1
                
        if i < n and not s[i].isupper():
            print("NO")
            return
            
    print("YES")

if __name__ == "__main__":
    main()
