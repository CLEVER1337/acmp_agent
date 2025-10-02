
def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        print(-1)
        return
        
    n = int(data[0])
    m = int(data[1])
    
    if n == 0 and m == 0:
        print(0)
        return
        
    if n % 2 != 0:
        print(-1)
        return
        
    attacks = 0
    heads = n
    tails = m
    
    while heads > 0 or tails > 0:
        if tails >= 2:
            tails -= 2
            heads += 1
            attacks += 1
        elif heads >= 2:
            heads -= 2
            attacks += 1
        elif tails == 1:
            tails += 1
            attacks += 1
        else:
            print(-1)
            return
            
    print(attacks)

if __name__ == "__main__":
    main()
