
def main():
    import sys
    n = int(sys.stdin.readline().strip())
    if n == 1:
        print("0")
        return
    if n == 2:
        print("0 1")
        return
    if n < 5:
        print("-1")
        return
        
    result = [0] * n
    left = 0
    right = n - 1
    value = 0
    
    for i in range(n):
        if i % 2 == 0:
            result[left] = value
            left += 1
        else:
            result[right] = value
            right -= 1
        value += 1
        
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()
