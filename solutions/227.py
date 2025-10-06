
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
        print(1)
        return
        
    if X == 0:
        if Y != 0:
            print(-1)
            return
            
    if Y < X:
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
                if buffer < current:
                    buffer = current
                    steps += 1
                else:
                    break
                    
    if current == Y:
        print(steps)
    else:
        print(-1)

if __name__ == "__main__":
    main()
