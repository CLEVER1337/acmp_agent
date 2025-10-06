
def main():
    b = int(input().strip())
    if b <= 3:
        print(-1)
        return
        
    n = b
    digits = [0] * n
    digits[0] = n - 2
    digits[n - 3] = 1
    digits[n - 1] = 1
    
    for i in range(n):
        print(digits[i])

if __name__ == "__main__":
    main()
