
def main():
    n = int(input().strip())
    if n == 1:
        print(0)
        return
    if n == 2:
        print("0 1")
        return
        
    result = [0] * n
    left = 0
    right = n - 1
    num = 0
    
    for i in range(n):
        if i % 2 == 0:
            result[left] = num
            left += 1
        else:
            result[right] = num
            right -= 1
        num += 1
        
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()
