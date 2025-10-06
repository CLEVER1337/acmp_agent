
def main():
    n = int(input().strip())
    if n == 1:
        print("0 0")
        return
        
    def remove_factors(number, factor):
        count = 0
        while number % factor == 0:
            count += 1
            number //= factor
        return count, number
        
    temp_n = n
    count2, temp_n = remove_factors(temp_n, 2)
    count5, temp_n = remove_factors(temp_n, 5)
    preperiod_length = max(count2, count5)
    
    if temp_n == 1:
        period_length = 0
    else:
        period_length = 1
        remainder = 10 % temp_n
        while remainder != 1:
            remainder = (remainder * 10) % temp_n
            period_length += 1
            
    print(f"{preperiod_length} {period_length}")

if __name__ == "__main__":
    main()
