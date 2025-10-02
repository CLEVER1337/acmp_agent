
def solve():
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
        print(1)
        return
        
    if X == 0:
        if Y != 0:
            print(-1)
            return
            
    if Y < X:
        print(-1)
        return
        
    if X == 0:
        print(-1)
        return
        
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
        
    if Y % gcd(X, Y - X) != 0:
        print(-1)
        return
        
    steps = 0
    current = X
    buffer = 0
    
    while current < Y:
        if buffer == 0:
            buffer = current
            steps += 1
        else:
            if current + buffer <= Y:
                current += buffer
                steps += 1
            else:
                if (Y - current) % buffer == 0:
                    steps += (Y - current) // buffer
                    current = Y
                else:
                    steps += 1
                    buffer = current
                    
    if current == Y:
        print(steps)
    else:
        print(-1)

if __name__ == "__main__":
    solve()
