
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    m = int(data[1])
    a = list(map(int, data[2:2+n]))
    
    total_burn = sum(a)
    max_burn = total_burn + n - 1
    
    if m < min(a) or m > max_burn:
        print("no")
        return
        
    min_time = 0
    max_time = 0
    for i in range(n):
        min_time += a[i]
        max_time += a[i] + 1
    
    min_time -= 1
    max_time -= 1
    
    if min_time <= m <= max_time:
        print("yes")
    else:
        print("no")

if __name__ == "__main__":
    main()
