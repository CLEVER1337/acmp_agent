
def main():
    with open("INPUT.TXT", "r") as f:
        n, m = map(int, f.readline().split())
    
    if n == 0 and m == 0:
        print(0)
        return
        
    if n % 2 == 1:
        print(-1)
        return
        
    hits = 0
    heads = n
    tails = m
    
    while heads > 0 or tails > 0:
        if tails % 2 == 1:
            tails += 1
            hits += 1
            
        if heads > 0:
            heads -= 2
            hits += 1
        else:
            tails -= 2
            hits += 1
            
    print(hits)

if __name__ == "__main__":
    main()
