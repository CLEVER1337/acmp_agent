
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    d = int(data[1])
    masses = list(map(int, data[2:2+n]))
    
    masses.sort()
    left = 0
    right = n - 1
    boats = 0
    
    while left <= right:
        if masses[left] + masses[right] <= d:
            left += 1
        right -= 1
        boats += 1
        
    print(boats)

if __name__ == "__main__":
    main()
