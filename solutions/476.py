
def main():
    import sys
    data = sys.stdin.read().split()
    M = int(data[0])
    N = int(data[1])
    
    k = 0
    while M > 1 and N > 1:
        k += 1
        M -= 1
        N -= 1
        
    if k % 2 == 0:
        print(1)
    else:
        print(2)

if __name__ == "__main__":
    main()
