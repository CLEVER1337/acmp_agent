
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
    
    washes = 0
    current_components = set()
    
    for juice in juices:
        if not current_components.issubset(juice):
            washes += 1
            current_components = juice.copy()
        else:
            current_components = juice.copy()
    
    washes += 1
    print(washes)

if __name__ == "__main__":
    main()
