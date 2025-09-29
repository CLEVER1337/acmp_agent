
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    m = int(data[1])
    costs = list(map(int, data[2:2+n]))
    
    costs.sort(reverse=True)
    total = 0
    count = 0
    
    for cost in costs:
        if count >= m:
            break
        if cost > 0:
            total += cost
            count += 1
        else:
            break
    
    print(total)

if __name__ == "__main__":
    main()
