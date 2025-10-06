
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    m = int(data[1])
    k = int(data[2])
    
    total_icons = 0
    for _ in range(n):
        x = m
        red_needed = x // k
        white_needed = x % k
        if white_needed > k - 1:
            red_needed += 1
            white_needed = 0
        total_icons += red_needed + white_needed
    
    print(total_icons)

if __name__ == "__main__":
    main()
