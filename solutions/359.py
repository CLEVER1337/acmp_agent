
def main():
    n = int(input().strip())
    if n == 1:
        print(1)
        return
        
    a, b = 1, 2
    direction = 1
    current_col = 2
    current_num = 2
    
    while current_col < n:
        if direction == 1:
            steps = a + 1
            a += 1
            current_num += steps
            direction = -1
        else:
            steps = b + 1
            b += 1
            current_num += steps
            direction = 1
        current_col += 1
        
    print(current_num)

if __name__ == "__main__":
    main()
