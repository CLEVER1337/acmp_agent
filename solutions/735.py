
def main():
    S = input().strip()
    T = input().strip()
    n = len(S)
    m = len(T)
    
    if m == 0:
        print("YES")
        return
        
    for start in range(n):
        pos = start
        valid = True
        for char in T:
            if pos >= n:
                pos = 0
            if char != S[pos]:
                valid = False
                break
            pos += 1
            
        if valid:
            print("YES")
            return
            
    print("NO")

if __name__ == "__main__":
    main()
