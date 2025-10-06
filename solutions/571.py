
def main():
    n = int(input().strip())
    directions = list(map(int, input().split()))
    
    if n % 3 != 0:
        print(0)
        return
        
    side_length = n // 3
    count = 0
    
    for start in range(n):
        valid = True
        for i in range(side_length):
            pos1 = (start + i) % n
            pos2 = (start + i + side_length) % n
            pos3 = (start + i + 2 * side_length) % n
            
            if directions[pos1] != directions[pos2] or directions[pos1] != directions[pos3]:
                valid = False
                break
                
        if valid:
            count += 1
            
    print(count)

if __name__ == "__main__":
    main()
