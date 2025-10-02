
def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        print(-1)
        return
        
    n = int(data[0])
    a = list(map(int, data[1:1+n]))
    b = list(map(int, data[1+n:1+2*n]))
    
    indices = list(range(n))
    indices.sort(key=lambda i: (b[i], a[i]))
    
    total_time = 0
    for i in indices:
        total_time += a[i]
        if total_time > b[i]:
            print(-1)
            return
            
    print(' '.join(map(str, [i+1 for i in indices])))

if __name__ == "__main__":
    main()
