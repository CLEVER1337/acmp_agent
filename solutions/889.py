
def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        return
    
    k = int(data[0])
    m = int(data[1])
    connections = []
    index = 2
    for i in range(m):
        p = int(data[index])
        h = int(data[index+1])
        index += 2
        connections.append((p, h))
    
    connections.sort(key=lambda x: x[1], reverse=True)
    
    left = k
    right = k
    
    for p, h in connections:
        if p >= left - 1 and p <= right:
            if p == left - 1:
                left = p
            elif p == right:
                right = p + 1
            else:
                if p - left + 1 < right - p:
                    left = p
                else:
                    right = p + 1
    
    print(left)

if __name__ == "__main__":
    main()
