
def main():
    n = int(input().strip())
    if n == 0:
        print(1)
        return
        
    c = n & -n
    r = n + c
    result = r | (((n ^ r) // c) >> 2)
    print(result)

if __name__ == '__main__':
    main()
