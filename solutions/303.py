
def main():
    s = input().strip()
    n = len(s)
    max_sum = -10**18
    
    for i in range(n):
        num = list(s)
        del num[i]
        current_sum = 0
        sign = 1
        for j, digit in enumerate(num):
            current_sum += sign * int(digit)
            sign *= -1
        if current_sum > max_sum:
            max_sum = current_sum
            
    print(max_sum)

if __name__ == "__main__":
    main()
