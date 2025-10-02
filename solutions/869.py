
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    D = int(data[1])
    masses = list(map(int, data[2:2+n]))
    
    masses.sort()
    left = 0
    right = n - 1
    boats = 0
    
    while left <= right:
        if left == right:
            boats += 1
            break
            
        if masses[left] + masses[right] <= D:
            left += 1
            right -= 1
            boats += 1
        else:
            right -= 1
            boats += 1
            
    print(boats)

if __name__ == "__main__":
    main()
