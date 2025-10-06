
def main():
    n = int(input().strip())
    ships = []
    for _ in range(n):
        x, y, s = map(int, input().split())
        ships.append((x, y, s))
    
    left = -10**9
    right = 10**9
    bottom = -10**9
    top = 10**9
    
    for x, y, s in ships:
        a = x + y
        b = x - y
        
        min_a = a - s * 2
        max_a = a
        min_b = b - s
        max_b = b + s
        
        left = max(left, min_a)
        right = min(right, max_a)
        bottom = max(bottom, min_b)
        top = min(top, max_b)
    
    if left > right or bottom > top:
        print("0.000")
    else:
        area = (right - left) * (top - bottom) / 4.0
        if area < 0:
            print("0.000")
        else:
            print("{:.3f}".format(area))

if __name__ == "__main__":
    main()
