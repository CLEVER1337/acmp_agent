
def main():
    import sys
    data = sys.stdin.readline().split()
    N = int(data[0])
    M = int(data[1])
    
    count = [0] * 10
    
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            product = i * j
            while product > 0:
                digit = product % 10
                count[digit] += 1
                product //= 10
                
    for i in range(10):
        print(count[i])

if __name__ == "__main__":
    main()
