
def main():
    import sys
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    juices = []
    for i in range(1, n+1):
        parts = data[i].split()
        k = int(parts[0])
        components = set(parts[1:1+k])
        juices.append(components)
    
    washes = 1
    for i in range(1, n):
        if not juices[i].issuperset(juices[i-1]):
            washes += 1
            
    print(washes)

if __name__ == "__main__":
    main()
