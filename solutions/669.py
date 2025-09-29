
def main():
    with open('INPUT.TXT', 'r') as f:
        M = int(f.readline().strip())
    
    if M == 1:
        print("-1 -1")
        return
        
    factors = []
    n = M
    for d in range(9, 1, -1):
        while n % d == 0:
            factors.append(d)
            n //= d
            
    if n != 1:
        print("-1 -1")
        return
        
    factors.sort()
    min_num = int(''.join(map(str, factors)))
    
    factors.sort(reverse=True)
    max_num = int(''.join(map(str, factors)))
    
    print(f"{min_num} {max_num}")

if __name__ == "__main__":
    main()
