
def main():
    with open('INPUT.TXT', 'r') as f:
        data = f.read().splitlines()
    
    n, m = map(int, data[0].split())
    original = data[1:1+n]
    negative = data[2+n:2+n+n]
    
    count = 0
    for i in range(n):
        for j in range(m):
            original_pixel = original[i][j]
            negative_pixel = negative[i][j]
            
            if original_pixel == 'B':
                correct_negative = 'W'
            else:
                correct_negative = 'B'
                
            if negative_pixel != correct_negative:
                count += 1
                
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(count))

if __name__ == "__main__":
    main()
