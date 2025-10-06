
def main():
    import sys
    data = sys.stdin.read().split()
    N = int(data[0])
    K = int(data[1])
    
    total = 0
    for i in range(1, K + 1):
        rooms_on_side = i + 1
        total += N * (rooms_on_side - 1)
    
    total += 1
    print(total)

if __name__ == "__main__":
    main()
