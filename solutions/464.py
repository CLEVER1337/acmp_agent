
def main():
    n = int(input().strip())
    if n == 1:
        print(0)
        return
        
    length = 1
    k = 0
    while length < n:
        k += 1
        length = 2 * length
        
    def find_digit(pos, level, value):
        if level == 0:
            return value
            
        half = 1 << (level - 1)
        if pos <= half:
            return find_digit(pos, level - 1, value)
        else:
            return find_digit(pos - half, level - 1, (value + 1) % 3)
            
    result = find_digit(n, k, 0)
    print(result)

if __name__ == "__main__":
    main()
