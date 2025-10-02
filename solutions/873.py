
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    m = int(data[1])
    
    k = n // 2
    result = pow(2, k * k, m)
    print(result)

if __name__ == "__main__":
    main()
