
def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        print(-1)
        return
        
    X = int(data[0])
    Y = int(data[1])
    
    if X == Y:
        print(0)
        return
        
    if Y == 0:
        if X == 0:
            print(0)
        else:
            print(-1)
        return
        
    if X == 0:
        print(-1)
        return
        
    if Y % X != 0:
        print(-1)
        return
        
    k = Y // X
    if k <= 0:
        print(-1)
        return
        
    count = 0
    while k > 1:
        if k % 2 == 1:
            print(-1)
            return
        k //= 2
        count += 1
        
    print(count + 1)

if __name__ == "__main__":
    main()
