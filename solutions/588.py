
def main():
    b = int(input())
    if b <= 3:
        print(-1)
        return
        
    digits = [0] * b
    digits[0] = b - 4
    digits[1] = 2
    digits[2] = 1
    digits[b-4] = 1
    
    for i in range(b):
        print(digits[i])

if __name__ == "__main__":
    main()
