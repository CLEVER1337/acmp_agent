
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    heights = list(map(int, data[1:1+n]))
    
    heights.sort()
    if n % 2 == 1:
        median = heights[n//2]
    else:
        median = (heights[n//2 - 1] + heights[n//2]) / 2.0
        
    print("{:.6f}".format(median))

if __name__ == "__main__":
    main()
