
def last_nonzero_digit(n):
    if n == 0:
        return 1
    
    res = 1
    count2 = 0
    count5 = 0
    
    for i in range(1, n + 1):
        num = i
        while num % 2 == 0:
            count2 += 1
            num //= 2
        while num % 5 == 0:
            count5 += 1
            num //= 5
        res = (res * num) % 10
    
    excess_2 = count2 - count5
    for _ in range(excess_2):
        res = (res * 2) % 10
    
    return res

def main():
    with open('INPUT.TXT', 'r') as f:
        n = int(f.read().strip())
    
    result = last_nonzero_digit(n)
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(result))

if __name__ == '__main__':
    main()
