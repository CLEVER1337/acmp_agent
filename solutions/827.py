
def main():
    import sys
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    juices = []
    index = 1
    for i in range(n):
        parts = data[index].split()
        index += 1
        k = int(parts[0])
        components = set(parts[1:1+k])
        juices.append(components)
    
    washes = 0
    current_set = set()
    
    for juice in juices:
        if not current_set.issubset(juice):
            washes += 1
            current_set = juice.copy()
        else:
            current_set = juice.copy()
            
    washes += 1
    print(washes)

if __name__ == "__main__":
    main()
