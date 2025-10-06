
def main():
    import sys
    data = sys.stdin.readline().split()
    N = int(data[0])
    M = int(data[1])
    
    if M == 1:
        print(N)
        return
        
    count = 0
    while N > 0 and M > 1:
        if M % 2 == 0:
            count += N // 2
            N = (N + 1) // 2
            M = M // 2
        else:
            count += (N + 1) // 2
            N = N // 2
            M = (M + 1) // 2
            
    print(count + 1)

if __name__ == "__main__":
    main()
