
def main():
    import sys
    data = sys.stdin.readline().split()
    N = int(data[0])
    K = int(data[1])
    
    for _ in range(K):
        next_N = N + bin(N).count('1')
        if next_N == N:
            break
        N = next_N
        
    print(N)

if __name__ == "__main__":
    main()
