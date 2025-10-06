
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    m = int(data[1])
    a = list(map(int, data[2:2+n]))
    
    total = sum(a)
    min_time = total - (n - 1)
    max_time = total
    
    if m < min_time or m > max_time:
        print("no")
        return
        
    print("yes")

if __name__ == "__main__":
    main()
