
def main():
    n = int(input().strip())
    if n == 1:
        print(0)
        return
        
    result = n
    temp = n
    i = 2
    while i * i <= temp:
        if temp % i == 0:
            while temp % i == 0:
                temp //= i
            result -= result // i
        i += 1
        
    if temp > 1:
        result -= result // temp
        
    print(result)

if __name__ == "__main__":
    main()
