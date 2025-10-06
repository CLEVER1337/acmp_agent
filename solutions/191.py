
def main():
    n = int(input().strip())
    if n == 1:
        print("1")
        return
        
    count = 1
    digits = [1]
    
    while count < n:
        i = len(digits) - 1
        while i >= 0 and digits[i] == 9:
            i -= 1
            
        if i == -1:
            digits = [1] * (len(digits) + 1)
        else:
            digits[i] += 1
            for j in range(i + 1, len(digits)):
                digits[j] = digits[i]
                
        count += 1
        
    print(''.join(map(str, digits)))

if __name__ == "__main__":
    main()
