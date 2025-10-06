
def main():
    S = input().strip()
    T = input().strip()
    
    if not T:
        return
        
    n = len(S)
    m = len(T)
    
    if m > n:
        return
        
    positions = []
    for i in range(n - m + 1):
        if S[i:i+m] == T:
            positions.append(str(i))
            
    print(' '.join(positions))

if __name__ == "__main__":
    main()
