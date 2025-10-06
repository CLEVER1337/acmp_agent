
def main():
    data = input().split()
    C = data[0]
    N = int(data[1])
    
    left = []
    right = []
    
    if C == 'L':
        left.append(N)
    else:
        right.append(N)
    
    base = 1
    while N > 0:
        remainder = N % 3
        if remainder == 1:
            right.append(base)
            N -= 1
        elif remainder == 2:
            left.append(base)
            N += 1
        N //= 3
        base *= 3
    
    if C == 'L':
        left.remove(N)
    else:
        right.remove(N)
    
    left.sort()
    right.sort()
    
    print("L:", ' '.join(map(str, left)))
    print("R:", ' '.join(map(str, right)))

if __name__ == "__main__":
    main()
