
def solve():
    data = input().split()
    C = data[0]
    N = int(data[1])
    
    weights = []
    while N > 0:
        remainder = N % 3
        weights.append(remainder)
        N = N // 3
        
    weights.append(0)
    
    left = []
    right = []
    power = 1
    
    for i in range(len(weights)):
        if weights[i] == 0:
            pass
        elif weights[i] == 1:
            if C == 'L':
                right.append(power)
            else:
                left.append(power)
        elif weights[i] == 2:
            if C == 'L':
                left.append(power)
                weights[i+1] += 1
            else:
                right.append(power)
                weights[i+1] += 1
        elif weights[i] == 3:
            weights[i+1] += 1
        
        power *= 3
    
    left.sort()
    right.sort()
    
    print("L:", end="")
    if left:
        print(" " + " ".join(map(str, left)))
    else:
        print()
    
    print("R:", end="")
    if right:
        print(" " + " ".join(map(str, right)))
    else:
        print()

solve()
