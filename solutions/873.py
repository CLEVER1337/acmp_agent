
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    m = int(data[1])
    
    k = n // 2
    total_patterns = pow(4, k * k, m)
    
    print(total_patterns % m)

if __name__ == "__main__":
    main()
