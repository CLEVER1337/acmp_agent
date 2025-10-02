
def main():
    with open("INPUT.TXT", "r") as f:
        s = f.readline().strip()
        t = f.readline().strip()
    
    n = len(s)
    m = len(t)
    
    if m == 0:
        print("YES")
        return
        
    if n == 0:
        print("NO")
        return
        
    for start in range(n):
        pos = 0
        for i in range(start, start + m):
            if s[i % n] != t[pos]:
                break
            pos += 1
            if pos == m:
                print("YES")
                return
                
    print("NO")

if __name__ == "__main__":
    main()
